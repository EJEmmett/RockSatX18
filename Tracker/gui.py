#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import font as tkFont
from urllib import request
from PIL import Image, ImageTk
import math
import numpy as np
from multiprocessing import Process, Queue
import email
import imaplib

class BeaconMapper(object):

    def __init__(self):
        ''' Init BeaconMapper: check for existing SBD files; read API key; set up the Tkinter window '''
        print('Start')

        #Login
        self.m = imaplib.IMAP4_SSL('imap.gmail.com')
        self.m.login("Ccprojecthermes@gmail.com", "Hermes123321#")
        self.m.select('INBOX')

        # Default values
        self._job = None # Keep track of timer calls
        self.zoom = '10' # Default Google Maps zoom (text)
        self.default_interval = 60 # Default update interval (secs)
        self.sep_width = 304 # Separator width in pixels
        self.map_lat = 37.844039 # Map latitude (degrees)
        self.map_lon = -75.483391 # Map longitude (degrees)
        self.frame_height = 480 # Google Static Map window width
        self.frame_width = 640 # Google Static Map window height
        self.delta_limit_pixels = 200 # If base to beacon angle (delta) exceeds this many pixels, decrease the zoom level accordingly
        self.map_type = 'hybrid' # Maps can be: roadmap , satellite , terrain or hybrid
        self.enable_clicks = False # Are mouse clicks enabled? False until first map has been loaded
        self.beacons = 0 # How many beacons are currently being tracked
        self.max_beacons = 8 # Track up to this many beacons
        self.beacon_imeis = {} # Dictionary of the serial numbers of the beacons currently being tracked
        self.beacon_paths = [] # List of beacon paths for Static Map
        self.beacon_locations = [] # List of current location for each beacon
        # Colours for beacon markers and paths - supported by both Tkinter and Google Static Maps API
        self.beacon_colours = ['red','yellow','green','blue','purple','gray','brown','orange']
        self.coords = [0]*2
        # Limit path lengths to this many characters depending on how many beacons are being tracked
        # (Google allows combined URLs of up to 8192 characters)
        # The first entry is redundant (i.e. would be used when tracking zero beacons)
        # These limits take into account that each pipe ('|') is expanded to '%7C' by urllib
        self.max_path_lengths = [7000, 7000, 3400, 2200, 1600, 1300, 1050, 900, 780]
        self.past_url = ""
        self.changed_center = 0
        # Google static map API pixel scales to help with map moves
        # https://gis.stackexchange.com/questions/7430/what-ratio-scales-do-google-maps-zoom-levels-correspond-to
        # ---
        # Radius of the Earth at the Equator = 6378137m
        # Circumference at the Equator = 2*pi*r = 40075017m
        # Zoom level 24 uses 2^32 (4294967296) pixels at circumference
        # Pixel scale at zoom level 24 is 0.009330692m/pixel
        # Pixel scale doubles with each zoom level
        # Pixel scale at zoom level 21 is 0.074645535m/pixel
        # Pixel scale at zoom level 1 is 78271.5170m/pixel
        # ---
        # Zoom level 24 uses 2^32 (4294967296) pixels at circumference
        # Each pixel represents an angle of 2*pi/2^32 radians = 1.46291808e-9 radians
        # Angle doubles with each zoom level
        # Zoom level 21 is 1.17033446e-8 radians per pixel
        # In degrees:
        # Zoom level 21 is 6.70552254e-7 degrees per pixel
        # Zoom level 1 is 0.703125 degrees per pixel
        # ---
        # These values need to be adjusted with increasing latitude due to the Mercator projection
        self.scales = np.array([
            [1,7.03125000E-01], # Zoom level 1 is 0.703125 degrees per pixel at the Equator
            [2,3.51562500E-01],
            [3,1.75781250E-01],
            [4,8.78906250E-02],
            [5,4.39453125E-02],
            [6,2.19726562E-02],
            [7,1.09863281E-02],
            [8,5.49316406E-03],
            [9,2.74658203E-03],
            [10,1.37329102E-03],
            [11,6.86645508E-04],
            [12,3.43322754E-04],
            [13,1.71661377E-04],
            [14,8.58306885E-05],
            [15,4.29153442E-05],
            [16,2.14576721E-05],
            [17,1.07288361E-05],
            [18,5.36441803E-06],
            [19,2.68220901E-06],
            [20,1.34110451E-06],
            [21,6.70552254E-07]]) # Zoom level 21 is 6.70552254e-7 degrees per pixel at the Equator

        # Set up Tkinter GUI
        self.window = tk.Tk() # Create main window
        self.window.wm_title("Iridium 9603N Mapper") # Add a title
        self.window.config(background="#FFFFFF") # Set background colour to white

        # Set up Frames
        self.toolFrame = tk.Frame(self.window, height=self.frame_height) # Frame for buttons and entries
        self.toolFrame.pack(side=tk.LEFT)

        self.imageFrame = tk.Frame(self.window, width=self.frame_width, height=self.frame_height) # Frame for map image
        self.imageFrame.pack(side=tk.RIGHT)

        # Load default blank image into imageFrame
        # Image must be self.frame_width x self.frame_height pixels
        filename = "map_image_blank.png"
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.imageFrame,image=photo)
        self.label.pack(fill=tk.BOTH) # Make the image fill the frame
        self.image = photo # Store the image to avoid garbage collection
        self.label.bind("<Button-1>",self.left_click) # Left mouse button click event
        self.label.bind("<Button-3>",self.right_click) # Right mouse button click event

        row = 0

        # Separator
        self.sep_1 = tk.Frame(self.toolFrame,height=1,bg='#808080',width=self.sep_width)
        self.sep_1.grid(row=row, columnspan=2)
        row += 1

        # Beacon location
        self.beacon_location = tk.Entry(self.toolFrame)
        self.beacon_location.grid(row=row, column=1)
        self.beacon_location.delete(0, tk.END)
        self.beacon_location.config(justify=tk.CENTER,width=22,state='readonly')
        self.beacon_location_txt = tk.Label(self.toolFrame, text = 'Beacon location',width=20)
        self.beacon_location_txt.grid(row=row, column=0)
        row += 1

        # Separator
        self.sep_2 = tk.Frame(self.toolFrame,height=1,bg='#808080',width=self.sep_width)
        self.sep_2.grid(row=row, columnspan=2)
        row += 1

        # Buttons
        self.boldFont = tkFont.Font(size=9,weight='bold')
        self.zoom_in_button = tk.Button(self.toolFrame, text="Zoom +", font=self.boldFont, width=20, height=1, command=self.zoom_map_in, state='disabled')
        self.zoom_in_button.grid(row=row,column=0)
        self.zoom_out_button = tk.Button(self.toolFrame, text="Zoom -", font=self.boldFont, width=20, height=1, command=self.zoom_map_out, state='disabled')
        self.zoom_out_button.grid(row=row+1,column=0)
        self.quit_button = tk.Button(self.toolFrame, text="Quit", font=self.boldFont, width=20, height=2, command=self.QUIT)
        self.quit_button.grid(row=row,column=1,rowspan=2)

        # Timer
        self.window.after(2000,self.timer) # First timer event after 2 secs

        # Start GUI
        self.window.mainloop()

    def timer(self):
        ''' Timer function - calls itself repeatedly to schedule map updates '''
        #if do_update: # If it is time to do an update
        self.update_coords()
        self.set_coords()
        self.update_map() # Update the Google Static Maps image

        self._job = self.window.after(100, self.timer) # Schedule another timer event in 0.25s

    def update_coords(self):
        typ, data = self.m.search(None, '(ON 8-Aug-2018 SUBJECT "SBD Msg From Unit: 300434063827480" UNSEEN)')
        for num in data[0].split():
            typ, message = self.m.fetch(num, '(RFC822)')
            body = message[0][1]
            mail = email.message_from_bytes(body)
            x = 0
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                if x%2:
                    pass
                else:
                    a = str(part.get_payload(decode=True)).replace("\\r\\n","").split("Unit Location: ")
                    b = a[1].split()
                    c = b[5].split("CEPradius")
                    self.coords[0] = float(b[2])
                    self.coords[1] = float(c[0])
                x += 1
            self.m.store(num, '+FLAGS', '\Seen')

    def set_coords(self):
        imei = "300434063827480"
        if self.coords != 0:
            latitude = self.coords[0]
            longitude = self.coords[1]
        else:
            return
        position_str = "{:.6f},{:.6f}".format(latitude, longitude) # Construct position
        if imei not in self.beacon_imeis:
            self.beacon_imeis[imei] = self.beacons # Add this imei and its beacon number
            self.beacon_paths.append('&path=color:'+self.beacon_colours[self.beacons]+'|weight:5') # Append an empty path for this beacon
            self.beacon_locations.append('') # Append a NULL location for this beacon
            self.beacons += 1 # Increment the number of beacons being tracked
            self.map_lat = latitude
            self.map_lon = longitude
        else:
            # Update beacon location
            self.beacon_locations[self.beacon_imeis[imei]] = position_str # Update location for this beacon
            # Change beacon location background colour
            self.beacon_location_txt.config(background=self.beacon_colours[self.beacon_imeis[imei]])

            # Update beacon path (append this location to the path for this beacon)
            self.beacon_paths[self.beacon_imeis[imei]] += '|' + position_str

            # Check path length hasn't exceeded the maximum
            def find_char(s, ch): # https://stackoverflow.com/a/11122355
                return [i for i, ltr in enumerate(s) if ltr == ch]
            while len(self.beacon_paths[self.beacon_imeis[imei]]) > self.max_path_lengths[self.beacons]:
                # Delete path from second to third pipe character ('|') (first '|' preceeds the line weight)
                pipes = find_char(self.beacon_paths[self.beacon_imeis[imei]],'|')
                self.beacon_paths[self.beacon_imeis[imei]] = self.beacon_paths[self.beacon_imeis[imei]][:pipes[1]] + self.beacon_paths[self.beacon_imeis[imei]][pipes[2]:]
            # Update beacon location
            self.beacon_location.config(state='normal')
            self.beacon_location.delete(0, tk.END)
            self.beacon_location.insert(0, position_str)
            self.beacon_location.config(state='readonly')

    def update_map(self):
        ''' Show beacon locations and the beacon routes using Google Maps API StaticMap '''

        # Assemble map center
        center = ("%.6f"%self.map_lat) + ',' + ("%.6f"%self.map_lon)
        # Update the Google Maps API StaticMap URL
        path_url = 'https://maps.googleapis.com/maps/api/staticmap?center=' # 54 chars
        path_url += center # 22 chars
        if self.beacons > 0: # Do we have any valid beacons?
            for beacon in range(self.beacons):
                path_url += '&markers=color:' + self.beacon_colours[beacon] + '|' # beacons*(15+6+3+22) chars
                path_url += self.beacon_locations[beacon]
           # Path 'header' is 29 chars
           # Minimum length for each waypoint is 18 chars but will grow to 20 when pipe is expanded
           # This needs to be included in the max_path_length
            for beacon in range(self.beacons):
                path_url += self.beacon_paths[beacon]
        path_url += '&zoom=' # 8 chars
        path_url += self.zoom
        path_url += '&size=' # 13 chars
        path_url += str(self.frame_width)
        path_url += 'x'
        path_url += str(self.frame_height)
        path_url += '&maptype=' + self.map_type + '&format=png' # 35 chars
        # Download the API map image from Google
        filename = "map_image.png" # Download map to this file
        try:
            if path_url != self.past_url:
                print(path_url)
                request.urlretrieve(path_url,filename)
            else:
                return
        except:
            filename = "map_image_blank.png" # If download failed, default to blank image

        # Update label using image
        image = Image.open(filename)
        photo = ImageTk.PhotoImage(image)
        self.label.configure(image=photo)
        self.image = photo

        # Enable zoom buttons and mouse clicks if a map image was displayed
        if filename == "map_image.png":
            self.zoom_in_button.config(state='normal') # Enable zoom+
            self.zoom_out_button.config(state='normal') # Enable zoom-
            self.enable_clicks = True # Enable mouse clicks
            self.past_url = path_url
        else: # Else disable them again
            self.zoom_in_button.config(state='disabled') # Disable zoom+
            self.zoom_out_button.config(state='disabled') # Disable zoom-
            self.enable_clicks = False # Disable mouse clicks

        # Update window
        self.window.update()

    def zoom_map_in(self):
        ''' Zoom in '''
        # Increment zoom if zoom is less than 21
        if int(self.zoom) < 21:
            self.zoom = str(int(self.zoom) + 1)
            self.update_map()

    def zoom_map_out(self):
        ''' Zoom out '''
        # Decrement zoom if zoom is greater than 0
        if int(self.zoom) > 0:
            self.zoom = str(int(self.zoom) - 1)
            self.update_map()

    def left_click(self, event):
        ''' Left mouse click - move map based on click position '''
        self.image_click(event, 'left')

    def right_click(self, event):
        ''' Right mouse click - copy map location to clipboard '''
        self.image_click(event, 'right')

    def image_click(self, event, button):
        ''' Handle mouse click event '''
        if (self.enable_clicks) and (int(self.zoom) > 0) and (int(self.zoom) <= 21): # Are clicks enabled and is zoom 1-21?
            x_move = event.x - (self.frame_width / 2) # Required x move in pixels
            y_move = event.y - (self.frame_height / 2) # Required y move in pixels
            scale_x = self.scales[np.where(int(self.zoom)==self.scales[:,0])][0][1] # Select scale from scales using current zoom
            # Compensate y scale (Mercator projection) using current latitude
            scale_multiplier_lat = math.cos(math.radians(self.map_lat))
            scale_y = scale_x * scale_multiplier_lat # Calculate y scale
            new_lat = self.map_lat - (y_move * scale_y) # Calculate new latitude
            new_lon = self.map_lon + (x_move * scale_x) # Calculate new longitude
            if button == 'left':
                self.map_lat = new_lat # Update lat
                self.map_lon = new_lon # Update lon
                self.update_map() # Update map
            else:
                # Copy the location to the clipboard so it can be pasted into (e.g.) a browser
                self.window.clipboard_clear() # Clear clipboard
                loc = ("%.6f"%new_lat) + ',' + ("%.6f"%new_lon) # Construct location
                self.window.clipboard_append(loc) # Copy location to clipboard
                self.window.update() # Update window

    def copy_location(self, imei):
        ''' Copy the location of this imei to the clipboard '''
        self.window.clipboard_clear() # Clear clipboard
        loc = self.beacon_locations[self.beacon_imeis[imei]] # Get location
        self.window.clipboard_append(loc) # Copy location to clipboard
        self.window.update() # Update window
        try:
            lat,lon = loc.split(',')
            self.map_lat = float(lat)
            self.map_lon = float(lon)
            self.update_map()
        except:
            pass

    def QUIT(self):
        ''' Quit the program '''
        if tkMessageBox.askokcancel("Quit", "Are you sure?"):
            self.window.destroy() # Destroy the window

if __name__ == "__main__":
    try:
        mapper = BeaconMapper()
    except KeyboardInterrupt:
        mapper.window.destroy()
