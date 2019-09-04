function Component()
{

}

Component.prototype.createOperations = function()
{
    component.createOperations();

    if (systemInfo.productType === "windows") {
        component.addOperation("CreateShortcut", "@TargetDir@/Lokkat.exe", "@StartMenuDir@/Lokkat.lnk",
            "workingDirectory=@TargetDir@", "iconPath=@TargetDir@/lokkat.ico", "description=Lokkat");
			
		component.addOperation("CreateShortcut", "@TargetDir@/Uninstall.exe", "@StartMenuDir@/Uninstall Lokkat.lnk",
            "workingDirectory=@TargetDir@", "description=Uninstall Lokkat");	

        try {
                var userProfile = installer.environmentVariable("USERPROFILE");
                installer.setValue("UserProfile", userProfile);
                component.addOperation("CreateShortcut", "@TargetDir@/Lokkat.exe", "@UserProfile@/Desktop/Lokkat.lnk", "description=Lokkat");
            } catch (e) {
                // Do nothing if key doesn't exist
            }
    }
}
