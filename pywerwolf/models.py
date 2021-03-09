
import typing as t
import enum

class GamePhase(enum.Enum):
    Setup = enum.auto()
    GameSetup = enum.auto()
    StartOfNight = enum.auto()
    NightPhase1 = enum.auto()
    NightPhase2 = enum.auto()
    NightPhase3 = enum.auto()
    NightPhase4 = enum.auto()
    NightPhase5 = enum.auto()
    NightEnd5 = enum.auto()
    ShowDead = enum.auto()
    Election = enum.auto()
    Discussion = enum.auto()
    Accuse = enum.auto()
    Poll = enum.auto()
    Voting = enum.auto()
    PollResult = enum.auto()
    Award = enum.auto()

class Roles(enum.Enum):
    NoRole = enum.auto()
    Villager = enum.auto()
    Werewolf = enum.auto()
    Seer = enum.auto()
    Witch = enum.auto()
    Hunter = enum.auto()
    Cupid = enum.auto()
    Protector = enum.auto()
    ParanormalInvestigator = enum.auto()
    Lycantrop = enum.auto()
    Spy = enum.auto()
    Murder = enum.auto()
    Pacifist = enum.auto()
    OldMan = enum.auto()
    Murder = enum.auto()
    Leaderwolf = enum.auto()

class Rules(object):
    showRoles: bool                       #`charaktereAufdecken` INT ( 2 ) DEFAULT 0,
    passMajor: bool                       #`buergermeisterWeitergeben` INT ( 2 ) DEFAULT 0,
    seerSeesIdentity: bool                #`seherSiehtIdentitaet` INT ( 2 ) DEFAULT 1,
    roleCount: t.Dict[Roles, int]
                                          #`werwolfzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`hexenzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`seherzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`jaegerzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`amorzahl` INT ( 2 ) DEFAULT 0 ,
                                          #`beschuetzerzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`parErmZahl` INT (5) DEFAULT 0 ,
                                          #`lykantrophenzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`spionezahl` INT ( 5 ) DEFAULT 0 ,
                                          #`idiotenzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`pazifistenzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`altenzahl` INT ( 5 ) DEFAULT 0 ,
                                          #`urwolfzahl` INT ( 5 ) DEFAULT 0 ,
    randomSelect: bool #`zufaelligeAuswahl` INT ( 2 ) DEFAULT 0 ,
    randomBonus: int #`zufaelligeAuswahlBonus` INT ( 5 ) DEFAULT 0 ,
    unanimously: bool #`werwolfeinstimmig` INT ( 2 ) DEFAULT 1 ,



class Player(object):
    role: Roles
    name: str
    leader: bool
    alive: bool
    ready: bool
    popup_text: str
    log: t.List[str]
    diedInRound: int
    accusedBy: "Player"


#                      `wahlAuf` INT ( 5 ) DEFAULT -1 ,
#                      `angeklagtVon` INT ( 5 ) DEFAULT -1 ,
#                      `nachtIdentitaet` INT( 10 ) NULL,
#                      `buergermeister` INT ( 2 ) DEFAULT 0,
#                      `hexeHeiltraenke` INT( 10 ) NULL,
#                      `hexeTodestraenke` INT( 5 ) NULL ,
#                      `hexenOpfer` INT ( 5 ) DEFAULT -1 ,
#                      `hexeHeilt` INT (2) DEFAULT 0,
#                      `beschuetzerLetzteRundeBeschuetzt` INT( 5 ) DEFAULT -1 ,
#                      `parErmEingesetzt` INT (2) DEFAULT 0 ,
#                      `verliebtMit` INT ( 5 ) DEFAULT -1 ,
#                      `jaegerDarfSchiessen` INT (2) DEFAULT 0 ,
#                      `buergermeisterDarfWeitergeben` INT (2) DEFAULT 0 ,
#                      `urwolf_anzahl_faehigkeiten` INT ( 5 ) DEFAULT 0,
#                      `countdownBis` INT (10) DEFAULT 0 ,
#                      `countdownAb` INT (10) DEFAULT 0 ,


class Game(object):
    currentPhase: GamePhase               #`spielphase` INT( 5 ) DEFAULT 0,
    gameRound: int
    rules: Rules
    log: t.List[str]
                                          #`werwolfopfer` INT ( 5 ) DEFAULT -1 ,
                                          #`werwolftimer1` INT ( 10 ) DEFAULT 60 ,
                                          #`werwolfzusatz1` INT ( 10 ) DEFAULT 4 ,
                                          #`werwolftimer2` INT ( 10 ) DEFAULT 50 ,
                                          #`werwolfzusatz2` INT ( 10 ) DEFAULT 3 ,
                                          #`dorftimer` INT ( 10 ) DEFAULT 550 ,
                                          #`dorfzusatz` INT ( 10 ) DEFAULT 10 ,
                                          #`dorfstichwahltimer` INT ( 10 ) DEFAULT 200 ,
                                          #`dorfstichwahlzusatz` INT ( 10 ) DEFAULT 5 ,
                                          #`inaktivzeit` INT ( 10 ) DEFAULT 40 ,
                                          #`inaktivzeitzusatz` INT ( 10 ) DEFAULT 0 ,
                                          #`tagestext` TEXT ,
                                          #`nacht` INT ( 5 ) DEFAULT 1 ,
                                          #`log` LONGTEXT ,
                                          #`list_lebe` LONGTEXT,
                                          #`list_lebe_aktualisiert` BIGINT DEFAULT 0,
                                          #`list_tot` LONGTEXT,
                                          #`list_tot_aktualisiert` BIGINT DEFAULT 0,
                                          #`waiting_for_others_time` BIGINT,
                                          #`letzterAufruf` BIGINT
