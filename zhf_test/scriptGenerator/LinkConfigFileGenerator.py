from zhf_test.scriptGenerator.ConfigFileGenerator import ConfigFileGenerator
from zhf_test.common.ConstVariable import *
import os


class LinkConfigFileGenerator(ConfigFileGenerator):
    def __init__(self, data):
        self.data = data

    def generate(self) -> str:
        project_prefix = self.data.projectName + "." + "OsgEarthNet."
        final_str = "<config>"
        final_str += ENTER_AND_TAB
        for index, link in enumerate(self.data.allLinks.linkSet):
            if link.linkType == LINK_TYPE_SATELLITE_TO_SATELLITE:
                final_str += "<{} src-module='{}' src-gate='{}' dest-module='{}' dest-gate='{}' " \
                             "channel-type='{}' link-info='{}'/>". \
                    format(link.linkTypeStr, link.srcNode.sat_name,
                           "ethg["+str(link.node1EthNum)+"]", link.destNode.sat_name, "ethg["+str(link.node2EthNum)+"]",
                           project_prefix + link.bandwidth, link.interOrIntraStr)
            elif link.linkType == LINK_TYPE_SATELLITE_TO_GROUNDSTATION:
                final_str += "<{} src-module='{}' src-gate='{}' dest-module='{}' dest-gate='{}' " \
                             "channel-type='{}' link-info='{}'/>". \
                    format(link.linkTypeStr, link.srcNode.sat_name,
                           "ethg["+link.node1EthNum+"]", link.destNode.groundStationName, "ethg["+link.node2EthNum+"]",
                           project_prefix + link.bandwidth, link.interOrIntraStr)
            if index == len(self.data.allLinks.linkSet) - 1:
                final_str += ENTER
            else:
                final_str += ENTER_AND_TAB
        link_handover_latitude = 66.32
        final_str += TAB + f"<LinkHandoverLatitude>{link_handover_latitude}</LinkHandoverLatitude>" + ENTER
        final_str += "</config>"
        return final_str

    def writeIntoConfigFile(self, generate_file_path=""):
        if generate_file_path == "":
            generate_file_path = "./" + self.data.projectName + "/masterNodes/" + "link_config.xml"
        else:
            generate_file_path = generate_file_path
        super(LinkConfigFileGenerator, self).writeIntoConfigFile(generate_file_path)
