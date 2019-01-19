import maya.cmds as cmds

##Check if a window already exists
if cmds.window('BoidsSimulation', exists=True):
        cmds.deleteUI('BoidsSimulation')

##Create a new window
window = cmds.window( title="BoidsSimulation", iconName='Boids' )
cmds.columnLayout( adjustableColumn=True )
cmds.setParent( '..' )

##Set the orientation of buttons
cmds.paneLayout( configuration='vertical2' )

##Seting up the buttons
leftMenuBarLayout = cmds.menuBarLayout()
leftMenu = cmds.menu( label='' )
cmds.text( label = 'Controls \n' )
cmds.menuItem( label='One' )

##Select number of boids to simulate, int slider
cmds.intSliderGrp( field=True, label='Number of boids', minValue=1, maxValue=100, fieldMinValue=-10, fieldMaxValue=110, value=1 )


##Set the speed of the boids
cmds.intSliderGrp( field=True, label='Speed', minValue=1, maxValue=20, fieldMinValue=-10, fieldMaxValue=20, value=1 )


##Close the window 
cmds.text( label='\n')
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.showWindow( window )
