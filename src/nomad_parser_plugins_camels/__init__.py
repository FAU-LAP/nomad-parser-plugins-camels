from pydantic import Field
from nomad.config.models.plugins import ParserEntryPoint


class MyParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_parser_plugins_camels.camels_parser import CamelsParser

        return CamelsParser(**self.dict())


myparser = MyParserEntryPoint(
    name = 'MyParser',
    description = 'My custom parser.',
    mainfile_name_re = '.*\.myparser',
)