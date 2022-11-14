from ..scriptGenerator.ConfigFileGenerator import ConfigFileGenerator
from zhf_test.common.ConstVariable import IniFilePre, ENTER


class IniFileGenerator(ConfigFileGenerator):
    def __init__(self, data):
        self.data = data

    def generate(self) -> str:
        final_str = ""
        final_str += IniFilePre
        """
        # 进行统一的卫星的参数的设置
        *.sat*.mobility.labelColor ="#ffff00ff"
        *.sat*.mobility.typename ="SatMobility"
        *.sat*.mobility.modelURL="satellite.osgb"
        *.sat*.mobility.modelScale=78000
        """
        satellite_name_prefix = self.data.allConstellations[0].consName
        final_str += "*." + satellite_name_prefix + "*" + ".mobility.labelColor = \"#ffff00ff\"" + ENTER
        final_str += "*." + satellite_name_prefix + "*" + ".mobility.typename = \"SatMobility\"" + ENTER
        final_str += "*." + satellite_name_prefix + "*" + ".mobility.modelURL = \"satellite.osgb\"" + ENTER
        final_str += "*." + satellite_name_prefix + "*" + ".mobility.modelScale = 78000" + ENTER + ENTER
        # 遍历所有的地面站
        for ground_station in self.data.allGroundStations:
            final_str += f"OsgEarthNet.{ground_station.groundStationName}.mobility.latitude = {ground_station.latitude}"
            final_str += ENTER
            final_str += f"OsgEarthNet.{ground_station.groundStationName}.mobility.latitude = {ground_station.latitude}"
            final_str += ENTER
        # 遍历所有的卫星
        for satellite in self.data.allConstellations[0].nodes:
            orbit_normal_str = ""
            for index, item in enumerate(satellite.orbit_normal):
                if index < 2:
                    orbit_normal_str += str(item) + ","
                else:
                    orbit_normal_str += str(item)
            final_str += f"OsgEarthNet.{satellite.sat_name}.mobility.orbitNormal = \"{orbit_normal_str}\""
            final_str += ENTER
            final_str += f"OsgEarthNet.{satellite.sat_name}.mobility.startingPhase = {satellite.starting_phase}deg"
            final_str += ENTER
            final_str += f"OsgEarthNet.{satellite.sat_name}.mobility.altitude = {satellite.altitude}km"
            final_str += ENTER
        return final_str

    def writeIntoConfigFile(self, generate_file_path):
        if generate_file_path == "":
            generate_file_path = "./" + self.data.projectName + "/masterNodes/" + "omnetpp.ini"
        else:
            generate_file_path = generate_file_path
        super(IniFileGenerator, self).writeIntoConfigFile(generate_file_path)
