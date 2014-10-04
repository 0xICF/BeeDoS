# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BeeDoS v1.0 Beta - Powered by 0xICF", pos = wx.DefaultPosition, size = wx.Size( 911,924 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		main_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		header_gSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.monkey = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"images/banner.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		header_gSizer.Add( self.monkey, 0, wx.ALL, 5 )
		
		
		main_bSizer.Add( header_gSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		body_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		body_fgSizer.SetFlexibleDirection( wx.BOTH )
		body_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		general_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"General" ), wx.VERTICAL )
		
		general_fgSizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		general_fgSizer.SetFlexibleDirection( wx.BOTH )
		general_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.server_staticText = wx.StaticText( self, wx.ID_ANY, u"Target server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.server_staticText.Wrap( -1 )
		general_fgSizer.Add( self.server_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.server = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.server.SetMinSize( wx.Size( 140,-1 ) )
		
		general_fgSizer.Add( self.server, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.verbose = wx.CheckBox( self, wx.ID_ANY, u"Verbose", wx.DefaultPosition, wx.DefaultSize, 0 )
		general_fgSizer.Add( self.verbose, 0, wx.ALL, 5 )
		
		self.port_staticText = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.port_staticText.Wrap( -1 )
		general_fgSizer.Add( self.port_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.port = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.port.SetMinSize( wx.Size( 140,-1 ) )
		
		general_fgSizer.Add( self.port, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		general_sbSizer.Add( general_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		attack_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Attack type" ), wx.VERTICAL )
		
		attack_fgSizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		attack_fgSizer.SetFlexibleDirection( wx.BOTH )
		attack_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.SlowHTTPChunked = wx.RadioButton( self, wx.ID_ANY, u"SlowHTTPChunked", wx.DefaultPosition, wx.DefaultSize, 0 )
		attack_fgSizer.Add( self.SlowHTTPChunked, 0, wx.ALL, 5 )
		
		self.Slowloris = wx.RadioButton( self, wx.ID_ANY, u"Slowloris", wx.DefaultPosition, wx.DefaultSize, 0 )
		attack_fgSizer.Add( self.Slowloris, 0, wx.ALL, 5 )
		
		self.Custom = wx.RadioButton( self, wx.ID_ANY, u"Custom", wx.DefaultPosition, wx.DefaultSize, 0 )
		attack_fgSizer.Add( self.Custom, 0, wx.ALL, 5 )
		
		
		attack_sbSizer.Add( attack_fgSizer, 1, wx.EXPAND, 5 )
		
		
		general_sbSizer.Add( attack_sbSizer, 1, wx.EXPAND|wx.ALL, 5 )
		
		threads_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Threads" ), wx.VERTICAL )
		
		threads_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		threads_fgSizer.SetFlexibleDirection( wx.BOTH )
		threads_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.threadsNum_staticText = wx.StaticText( self, wx.ID_ANY, u"Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.threadsNum_staticText.Wrap( -1 )
		threads_fgSizer.Add( self.threadsNum_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.threadsNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		threads_fgSizer.Add( self.threadsNum, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.threadsInt_staticText = wx.StaticText( self, wx.ID_ANY, u"Interval between threads", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.threadsInt_staticText.Wrap( -1 )
		threads_fgSizer.Add( self.threadsInt_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.threadsInt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		threads_fgSizer.Add( self.threadsInt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.threadsPerClient_staticText = wx.StaticText( self, wx.ID_ANY, u"Threads per Client", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.threadsPerClient_staticText.Wrap( -1 )
		threads_fgSizer.Add( self.threadsPerClient_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.threadsPerClient = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		threads_fgSizer.Add( self.threadsPerClient, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		threads_sbSizer.Add( threads_fgSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		general_sbSizer.Add( threads_sbSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		chunked_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Chunked data" ), wx.VERTICAL )
		
		chunked_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		chunked_fgSizer.SetFlexibleDirection( wx.BOTH )
		chunked_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.body_staticText = wx.StaticText( self, wx.ID_ANY, u"HTTP Body length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.body_staticText.Wrap( -1 )
		chunked_fgSizer.Add( self.body_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.body = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.body.SetMinSize( wx.Size( 140,-1 ) )
		
		chunked_fgSizer.Add( self.body, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chunkSize_staticText = wx.StaticText( self, wx.ID_ANY, u"Chunk size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chunkSize_staticText.Wrap( -1 )
		chunked_fgSizer.Add( self.chunkSize_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chunkSize = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chunkSize.SetMinSize( wx.Size( 140,-1 ) )
		
		chunked_fgSizer.Add( self.chunkSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chunksInt_staticText = wx.StaticText( self, wx.ID_ANY, u"Interval between chunks (ms)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chunksInt_staticText.Wrap( -1 )
		chunked_fgSizer.Add( self.chunksInt_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chunksInt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chunksInt.SetMinSize( wx.Size( 140,-1 ) )
		
		chunked_fgSizer.Add( self.chunksInt, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		chunked_sbSizer.Add( chunked_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		general_sbSizer.Add( chunked_sbSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		body_fgSizer.Add( general_sbSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		HTTP_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"HTTP Request" ), wx.VERTICAL )
		
		http_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		http_fgSizer.SetFlexibleDirection( wx.BOTH )
		http_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.host_staticText = wx.StaticText( self, wx.ID_ANY, u"Host header", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.host_staticText.Wrap( -1 )
		http_fgSizer.Add( self.host_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.host = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.host.SetMinSize( wx.Size( 200,-1 ) )
		
		http_fgSizer.Add( self.host, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.file_staticText = wx.StaticText( self, wx.ID_ANY, u"File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.file_staticText.Wrap( -1 )
		http_fgSizer.Add( self.file_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.file = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.file.SetMinSize( wx.Size( 200,-1 ) )
		
		http_fgSizer.Add( self.file, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ka = wx.CheckBox( self, wx.ID_ANY, u"Use Keep-Alive", wx.DefaultPosition, wx.DefaultSize, 0 )
		http_fgSizer.Add( self.ka, 0, wx.ALL, 5 )
		
		
		HTTP_sbSizer.Add( http_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		behavioral_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Behavioral configuration" ), wx.VERTICAL )
		
		fgSizer9 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.rUA = wx.CheckBox( self, wx.ID_ANY, u"Random User-Agents", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.rUA, 0, wx.ALL, 5 )
		
		self.rTI = wx.CheckBox( self, wx.ID_ANY, u"Random threads intervals", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.rTI, 0, wx.ALL, 5 )
		
		self.rCI = wx.CheckBox( self, wx.ID_ANY, u"Random chunks intervals", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.rCI, 0, wx.ALL, 5 )
		
		
		behavioral_sbSizer.Add( fgSizer9, 1, wx.EXPAND, 5 )
		
		
		HTTP_sbSizer.Add( behavioral_sbSizer, 1, wx.EXPAND|wx.ALL, 5 )
		
		request_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Request preview" ), wx.VERTICAL )
		
		self.request = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.HSCROLL|wx.NO_BORDER|wx.VSCROLL|wx.WANTS_CHARS )
		self.request.SetMinSize( wx.Size( 470,150 ) )
		self.request.SetMaxSize( wx.Size( 470,150 ) )
		
		request_sbSizer.Add( self.request, 1, wx.EXPAND |wx.ALL, 1 )
		
		
		HTTP_sbSizer.Add( request_sbSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		info_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		info_fgSizer.SetFlexibleDirection( wx.BOTH )
		info_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.info = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.HSCROLL|wx.NO_BORDER|wx.VSCROLL|wx.WANTS_CHARS )
		self.info.SetMinSize( wx.Size( 330,85 ) )
		self.info.SetMaxSize( wx.Size( -1,85 ) )
		
		info_fgSizer.Add( self.info, 1, wx.ALL|wx.EXPAND, 5 )
		
		info_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.attack = wx.Button( self, wx.ID_ANY, u"Attack", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.attack.SetMinSize( wx.Size( 120,-1 ) )
		
		info_bSizer.Add( self.attack, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.attackStop = wx.Button( self, wx.ID_ANY, u"Stop Attack", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.attackStop.SetMinSize( wx.Size( 120,-1 ) )
		
		info_bSizer.Add( self.attackStop, 0, wx.ALL, 5 )
		
		
		info_fgSizer.Add( info_bSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		HTTP_sbSizer.Add( info_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		body_fgSizer.Add( HTTP_sbSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		main_bSizer.Add( body_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		console_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Console" ), wx.VERTICAL )
		
		console_sbSizer.SetMinSize( wx.Size( -1,100 ) ) 
		console_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		console_fgSizer.SetFlexibleDirection( wx.BOTH )
		console_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.console = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.console.SetMinSize( wx.Size( 740,120 ) )
		self.console.SetMaxSize( wx.Size( 740,120 ) )
		
		console_fgSizer.Add( self.console, 1, wx.ALL|wx.EXPAND, 0 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.F5_bitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"images/ICFskeleton.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.F5_bitmap, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Powered by 0xICF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		console_fgSizer.Add( bSizer3, 1, wx.EXPAND|wx.LEFT, 5 )
		
		
		console_sbSizer.Add( console_fgSizer, 1, wx.EXPAND, 5 )
		
		
		main_bSizer.Add( console_sbSizer, 0, wx.ALL|wx.EXPAND, 10 )
		
		
		self.SetSizer( main_bSizer )
		self.Layout()
		self.BeeDoS_menubar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.exit_menuItem = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.AppendItem( self.exit_menuItem )
		
		self.BeeDoS_menubar.Append( self.file_menu, u"File" ) 
		
		self.help_menu = wx.Menu()
		self.about_menuItem = wx.MenuItem( self.help_menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.AppendItem( self.about_menuItem )
		
		self.BeeDoS_menubar.Append( self.help_menu, u"Help" ) 
		
		self.SetMenuBar( self.BeeDoS_menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.SlowHTTPChunked.Bind( wx.EVT_RADIOBUTTON, self.slowhttpchunkedAm )
		self.Slowloris.Bind( wx.EVT_RADIOBUTTON, self.slowlorisAm )
		self.Custom.Bind( wx.EVT_RADIOBUTTON, self.customAm )
		self.host.Bind( wx.EVT_TEXT, self.hostRef )
		self.file.Bind( wx.EVT_TEXT, self.fileRef )
		self.ka.Bind( wx.EVT_CHECKBOX, self.useKA )
		self.rUA.Bind( wx.EVT_CHECKBOX, self.rUAFunc )
		self.rTI.Bind( wx.EVT_CHECKBOX, self.rTIFunc )
		self.rCI.Bind( wx.EVT_CHECKBOX, self.rCIFunc )
		self.request.Bind( wx.EVT_TEXT, self.requestRef )
		self.attack.Bind( wx.EVT_BUTTON, self.startAttack )
		self.attackStop.Bind( wx.EVT_BUTTON, self.stopAttack )
		self.Bind( wx.EVT_MENU, self.exitFunc, id = self.exit_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.aboutFunc, id = self.about_menuItem.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def slowhttpchunkedAm( self, event ):
		event.Skip()
	
	def slowlorisAm( self, event ):
		event.Skip()
	
	def customAm( self, event ):
		event.Skip()
	
	def hostRef( self, event ):
		event.Skip()
	
	def fileRef( self, event ):
		event.Skip()
	
	def useKA( self, event ):
		event.Skip()
	
	def rUAFunc( self, event ):
		event.Skip()
	
	def rTIFunc( self, event ):
		event.Skip()
	
	def rCIFunc( self, event ):
		event.Skip()
	
	def requestRef( self, event ):
		event.Skip()
	
	def startAttack( self, event ):
		event.Skip()
	
	def stopAttack( self, event ):
		event.Skip()
	
	def exitFunc( self, event ):
		event.Skip()
	
	def aboutFunc( self, event ):
		event.Skip()
	

