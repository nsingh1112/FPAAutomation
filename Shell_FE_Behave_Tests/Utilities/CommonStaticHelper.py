import time
import os
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.TradeDealDESSalePageFunctions import \
    TradeDealDESSalePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.TradeDealFOBPurchasePageFunctions import \
    TradeDealFOBPurchasePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonControlFunctions.AssignToMyselfFunctions import \
    AssignToMyselfFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.CommonControlFunctions.LinkDealPopUpFunctions import \
    LinkDealPopUpFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.InternalVoyagePageFunctions import \
    InternalVoyagePageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.MasterPageFunctions import \
    MasterPageFunctions
from Shell_FE_Behave_Tests.ApplicationLibrary.FunctionalLibrary.PageFunctions.TradeDealFOBSalePageFunctions import \
    TradeDealFOBSalePageFunctions
from Shell_FE_Behave_Tests.Utilities.APIVoyageAndTradeDealLinkingHelper import APIVoyageAndTradeDealLinkingHelper
from Shell_FE_Behave_Tests.Utilities.DriverHelper import DriverHelper


class CommonStaticHelper:

    TradeDealPageUrl = "https://shell-energy-wona--fullcopy.lightning.force.com/lightning/r/SHL_Trade_Deal__c/"
    VoyagePageUrl = "https://shell-energy-wona--fullcopy.lightning.force.com/lightning/r/SHL_Voyage__c/"
    testFile1ToUploadPath = os.path.dirname(os.getcwd()) + "/Shell_FE_Behave_Tests/TestData/TestUpload1.pdf"
    terminalName = "Quintero LNG Terminal"

    @staticmethod
    def navigate_to_voyage(voyageId, driverInstance):
        driverInstance.get(CommonStaticHelper.VoyagePageUrl + voyageId + "/view")
        time.sleep(20)

    @staticmethod
    def navigate_to_deal(dealID, driverInstance):
        driverInstance.get(CommonStaticHelper.TradeDealPageUrl + dealID + "/view")
        time.sleep(80)

    @staticmethod
    def prerequisite_for_FOBDES():
        DriverHelper.bring_browser_to_focus(DriverHelper.driverInstanceFO)
        """ Open an internal voyage """
        internalVoyagePageFunctions = InternalVoyagePageFunctions(DriverHelper.driverInstanceFO)
        APIVoyageAndTradeDealLinkingHelper.get_voyage_from_API(True)
        masterPageFunctions = MasterPageFunctions(DriverHelper.driverInstanceFO)
        masterPageFunctions.search_the_item(APIVoyageAndTradeDealLinkingHelper.currentVoyageName)

        """Prior to linking of deal the operator must be assigned to purchase deal"""
        APIVoyageAndTradeDealLinkingHelper.get_trade_deal_for_FOB_DES_linking("FOB Purchase")
        DriverHelper.bring_browser_to_focus(DriverHelper.driverInstancePurchaseCO)
        masterPageFunctions = MasterPageFunctions(DriverHelper.driverInstancePurchaseCO)
        masterPageFunctions.search_the_item(APIVoyageAndTradeDealLinkingHelper.currentFobPurchaseDeal)
        tradeDealFOBPurchasePageFunctions = TradeDealFOBPurchasePageFunctions(
            DriverHelper.driverInstancePurchaseCO)
        tradeDealFOBPurchasePageFunctions.click_assign_to_myself()
        assignTo_MyselfFunctions = AssignToMyselfFunctions(DriverHelper.driverInstancePurchaseCO)
        assignTo_MyselfFunctions.click_on_save()

        """ User Links the FOB purchase trade deal """
        linkDealPopUpFunctions = LinkDealPopUpFunctions(DriverHelper.driverInstanceFO)
        DriverHelper.bring_browser_to_focus(DriverHelper.driverInstanceFO)
        internalVoyagePageFunctions.click_link_load_Deal()
        linkDealPopUpFunctions.select_tradeDeal(APIVoyageAndTradeDealLinkingHelper.currentFobPurchaseDeal)
        linkDealPopUpFunctions.click_on_link()

        """Prior to linking of deal the operator must be assigned"""
        APIVoyageAndTradeDealLinkingHelper.get_trade_deal_for_FOB_DES_linking("DES Sale")
        DriverHelper.bring_browser_to_focus(DriverHelper.driverInstanceSalesCO)
        masterPageFunctions = MasterPageFunctions(DriverHelper.driverInstanceSalesCO)
        masterPageFunctions.search_the_item(APIVoyageAndTradeDealLinkingHelper.currentDesSaleDeal)
        tradeDealDESSalePageFunctions = TradeDealDESSalePageFunctions(DriverHelper.driverInstanceSalesCO)
        tradeDealDESSalePageFunctions.click_assign_to_myself()
        AssignTo_MyselfFunctions = AssignToMyselfFunctions(DriverHelper.driverInstanceSalesCO)
        AssignTo_MyselfFunctions.click_on_save()

        """ User Links the DES sale trade deal """
        linkDealPopUpFunctions = LinkDealPopUpFunctions(DriverHelper.driverInstanceFO)
        DriverHelper.bring_browser_to_focus(DriverHelper.driverInstanceFO)
        internalVoyagePageFunctions.click_link_Discharge_Deal()
        linkDealPopUpFunctions.select_tradeDeal(APIVoyageAndTradeDealLinkingHelper.currentDesSaleDeal)
        linkDealPopUpFunctions.click_on_link()


    @staticmethod
    def prerequisite_for_FOBFOB():
        """Purchase CO logged in and Search for the FOB Purchase deal and Assign the Operator """
        APIVoyageAndTradeDealLinkingHelper.get_trade_deal_for_FOB_FOB_linking(False)
        DriverHelper.bring_browser_to_focus(DriverHelper.driverInstancePurchaseCO)
        CommonStaticHelper.navigate_to_deal(APIVoyageAndTradeDealLinkingHelper.currentFobPurchaseDealID,
                                            DriverHelper.driverInstancePurchaseCO)
        tradeDealFOBPurchasePageFunctions = TradeDealFOBPurchasePageFunctions(DriverHelper.driverInstancePurchaseCO)
        tradeDealFOBPurchasePageFunctions.click_assign_to_myself()
        AssignTo_MyselfFunctions = AssignToMyselfFunctions(DriverHelper.driverInstancePurchaseCO)
        AssignTo_MyselfFunctions.click_on_save()

        """Switched to Sales CO account and Search for the FOB Sale deal and Assign the operator """
        APIVoyageAndTradeDealLinkingHelper.get_trade_deal_for_FOB_FOB_linking(True)
        DriverHelper.bring_browser_to_focus(DriverHelper.driverInstanceSalesCO)
        CommonStaticHelper.navigate_to_deal(APIVoyageAndTradeDealLinkingHelper.currentFobSaleDealID,
                                            DriverHelper.driverInstanceSalesCO)
        tradeDealFOBSalePageFunctions = TradeDealFOBSalePageFunctions(DriverHelper.driverInstanceSalesCO)
        tradeDealFOBSalePageFunctions.click_assign_to_myself()
        AssignTo_MyselfFunctions = AssignToMyselfFunctions(DriverHelper.driverInstanceSalesCO)
        AssignTo_MyselfFunctions.click_on_save()

        """Sales CO Links the FOB purchase """
        linkDealPopUpFunctions = LinkDealPopUpFunctions(DriverHelper.driverInstanceSalesCO)
        tradeDealFOBSalePageFunctions.click_link_load_Deal()
        linkDealPopUpFunctions.select_tradeDeal(APIVoyageAndTradeDealLinkingHelper.currentFobPurchaseDeal)
        linkDealPopUpFunctions.click_on_link()

    @staticmethod
    def post_execution_of_FOBDES():
        if DriverHelper.driverInstanceFO is not None:
            DriverHelper.bring_browser_to_focus(DriverHelper.driverInstanceFO)
            internalVoyagePageFunctions = InternalVoyagePageFunctions(DriverHelper.driverInstanceFO)
            internalVoyagePageFunctions.navigate_to_tab("Freight Tracker")
            internalVoyagePageFunctions.unlink_the_load_deal()
            internalVoyagePageFunctions.unlink_the_discharge_deal()
