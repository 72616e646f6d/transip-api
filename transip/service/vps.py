""" The connector to VPS related API calls """

from transip.client import Client, MODE_RO, MODE_RW

class VpsService(Client):

    def __init__(self, *args, **kwargs):
        super(VpsService, self).__init__('VpsService', *args, **kwargs)

    def get_available_products(self):
        """ Get available VPS products """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableProducts')
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableProducts()

    def get_available_addons(self):
        """ Get available VPS addons """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableAddons')
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableAddons()

    def get_active_addons_for_vps(self, vpsName):
        """ Get all the Active Addons for Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getActiveAddonsForVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getActiveAddonsForVps(vpsName)

    def get_available_upgrades(self, vpsName):
        """ Get available VPS upgrades for a specific Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableUpgrades', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableUpgrades(vpsName)

    def get_available_addons_for_vps(self, vpsName):
        """ Get available Addons for Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableAddonsForVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableAddonsForVps(vpsName)

    def get_cancellable_addons_for_vps(self, vpsName):
        """ Get cancellable addons for specific Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getCancellableAddonsForVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getCancellableAddonsForVps(vpsName)

    def order_vps(self, productName, addons, operatingSystemName, hostname):
        """ Order a VPS with optional Addons """
        cookie = self.build_cookie(mode=MODE_RW, method='orderVps', parameters=[productName, addons, operatingSystemName, hostname])
        self.update_cookie(cookie)
        return self.soap_client.service.orderVps(productName, addons, operatingSystemName, hostname)

    def clone_vps(self, vpsName):
        """ Clone a VPS """
        cookie = self.build_cookie(mode=MODE_RW, method='cloneVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.cloneVps(vpsName)

    def order_addon(self, vpsName, addons):
        """ Order addons to a VPS """
        cookie = self.build_cookie(mode=MODE_RW, method='orderAddon', parameters=[vpsName, addons])
        self.update_cookie(cookie)
        return self.soap_client.service.orderAddon(vpsName, addons)

    def order_private_network(self):
        """ Order a private Network """
        cookie = self.build_cookie(mode=MODE_RW, method='orderPrivateNetwork')
        self.update_cookie(cookie)
        return self.soap_client.service.orderPrivateNetwork()

    def upgrade_vps(self, vpsName, upgradeToProductName):
        """ upgrade a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='upgradeVps', parameters=[vpsName, upgradeToProductName])
        self.update_cookie(cookie)
        return self.soap_client.service.upgradeVps(vpsName, upgradeToProductName)

    def cancel_vps(self, vpsName, endTime):
        """ Cancel a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='cancelVps', parameters=[vpsName, endTime])
        self.update_cookie(cookie)
        return self.soap_client.service.cancelVps(vpsName, endTime)

    def cancel_addon(self, vpsName, addonName):
        """ Cancel a Vps Addon """
        cookie = self.build_cookie(mode=MODE_RW, method='cancelAddon', parameters=[vpsName, addonName])
        self.update_cookie(cookie)
        return self.soap_client.service.cancelAddon(vpsName, addonName)

    def cancel_private_network(self, privateNetworkName, endTime):
        """ Cancel a PrivateNetwork """
        cookie = self.build_cookie(mode=MODE_RW, method='cancelPrivateNetwork', parameters=[privateNetworkName, endTime])
        self.update_cookie(cookie)
        return self.soap_client.service.cancelPrivateNetwork(privateNetworkName, endTime)

    def get_private_networks_by_vps(self, vpsName):
        """ Get Private networks for a specific vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getPrivateNetworksByVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getPrivateNetworksByVps(vpsName)

    def get_all_private_networks(self):
        """ Get all Private networks in your account """
        cookie = self.build_cookie(mode=MODE_RO, method='getAllPrivateNetworks')
        self.update_cookie(cookie)
        return self.soap_client.service.getAllPrivateNetworks()

    def add_vps_to_private_network(self, vpsName, privateNetworkName):
        """ Add VPS to a private Network """
        cookie = self.build_cookie(mode=MODE_RW, method='addVpsToPrivateNetwork', parameters=[vpsName, privateNetworkName])
        self.update_cookie(cookie)
        return self.soap_client.service.addVpsToPrivateNetwork(vpsName, privateNetworkName)

    def remove_vps_from_private_network(self, vpsName, privateNetworkName):
        """ Remove VPS from a private Network """
        cookie = self.build_cookie(mode=MODE_RW, method='removeVpsFromPrivateNetwork', parameters=[vpsName, privateNetworkName])
        self.update_cookie(cookie)
        return self.soap_client.service.removeVpsFromPrivateNetwork(vpsName, privateNetworkName)

    def get_traffic_information_for_vps(self, vpsName):
        """ Get Traffic information by vpsName for this contractPeriod """
        cookie = self.build_cookie(mode=MODE_RO, method='getTrafficInformationForVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getTrafficInformationForVps(vpsName)

    def start(self, vpsName):
        """ Start a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='start', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.start(vpsName)

    def stop(self, vpsName):
        """ Stop a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='stop', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.stop(vpsName)

    def reset(self, vpsName):
        """ Reset a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='reset', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.reset(vpsName)

    def create_snapshot(self, vpsName, description):
        """ Create a snapshot """
        cookie = self.build_cookie(mode=MODE_RW, method='createSnapshot', parameters=[vpsName, description])
        self.update_cookie(cookie)
        return self.soap_client.service.createSnapshot(vpsName, description)

    def revert_snapshot(self, vpsName, snapshotName):
        """ Revert a snapshot """
        cookie = self.build_cookie(mode=MODE_RW, method='revertSnapshot', parameters=[vpsName, snapshotName])
        self.update_cookie(cookie)
        return self.soap_client.service.revertSnapshot(vpsName, snapshotName)

    def revert_snapshot_to_other_vps(self, sourceVpsName, snapshotName, destinationVpsName):
        """ Revert a snapshot to another VPS """
        cookie = self.build_cookie(mode=MODE_RW, method='revertSnapshotToOtherVps', parameters=[sourceVpsName, snapshotName, destinationVpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.revertSnapshotToOtherVps(sourceVpsName, snapshotName, destinationVpsName)

    def remove_snapshot(self, vpsName, snapshotName):
        """ Remove a snapshot """
        cookie = self.build_cookie(mode=MODE_RW, method='removeSnapshot', parameters=[vpsName, snapshotName])
        self.update_cookie(cookie)
        return self.soap_client.service.removeSnapshot(vpsName, snapshotName)

    def revert_vps_backup(self, vpsName, vpsBackupId):
        """ Revert a vps backup """
        cookie = self.build_cookie(mode=MODE_RW, method='revertVpsBackup', parameters=[vpsName, vpsBackupId])
        self.update_cookie(cookie)
        return self.soap_client.service.revertVpsBackup(vpsName, vpsBackupId)

    def get_vps(self, vpsName):
        """ Get a Vps by name """
        cookie = self.build_cookie(mode=MODE_RO, method='getVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getVps(vpsName)

    def get_vpses(self):
        """ Get all Vpses """
        cookie = self.build_cookie(mode=MODE_RO, method='getVpses')
        self.update_cookie(cookie)
        return self.soap_client.service.getVpses()

    def get_snapshots_by_vps(self, vpsName):
        """ Get all Snapshots for a vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getSnapshotsByVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getSnapshotsByVps(vpsName)

    def get_vps_backups_by_vps(self, vpsName):
        """ Get all VpsBackups for a vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getVpsBackupsByVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getVpsBackupsByVps(vpsName)

    def get_operating_systems(self):
        """ Get all operating systems """
        cookie = self.build_cookie(mode=MODE_RO, method='getOperatingSystems')
        self.update_cookie(cookie)
        return self.soap_client.service.getOperatingSystems()

    def install_operating_system(self, vpsName, operatingSystemName, hostname):
        """ Install an operating system on a vps """
        cookie = self.build_cookie(mode=MODE_RW, method='installOperatingSystem', parameters=[vpsName, operatingSystemName, hostname])
        self.update_cookie(cookie)
        return self.soap_client.service.installOperatingSystem(vpsName, operatingSystemName, hostname)

    def install_operating_system_unattended(self, vpsName, operatingSystemName, base64InstallText):
        """ Install an operating system on a vps with a unattended installfile """
        cookie = self.build_cookie(mode=MODE_RW, method='installOperatingSystemUnattended', parameters=[vpsName, operatingSystemName, base64InstallText])
        self.update_cookie(cookie)
        return self.soap_client.service.installOperatingSystemUnattended(vpsName, operatingSystemName, base64InstallText)

    def get_ips_for_vps(self, vpsName):
        """ Get Ips for a specific Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='getIpsForVps', parameters=[vpsName])
        self.update_cookie(cookie)
        return self.soap_client.service.getIpsForVps(vpsName)

    def get_all_ips(self):
        """ Get All ips """
        cookie = self.build_cookie(mode=MODE_RO, method='getAllIps')
        self.update_cookie(cookie)
        return self.soap_client.service.getAllIps()

    def add_ipv6_to_vps(self, vpsName, ipv6Address):
        """ Add Ipv6 Address to Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='addIpv6ToVps', parameters=[vpsName, ipv6Address])
        self.update_cookie(cookie)
        return self.soap_client.service.addIpv6ToVps(vpsName, ipv6Address)

    def set_customer_lock(self, vpsName, enabled):
        """ Enable or Disable a Customer Lock for a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='setCustomerLock', parameters=[vpsName, enabled])
        self.update_cookie(cookie)
        return self.soap_client.service.setCustomerLock(vpsName, enabled)

    def handover_vps(self, vpsName, targetAccountname):
        """ Handover a VPS to another TransIP User """
        cookie = self.build_cookie(mode=MODE_RW, method='handoverVps', parameters=[vpsName, targetAccountname])
        self.update_cookie(cookie)
        return self.soap_client.service.handoverVps(vpsName, targetAccountname)
