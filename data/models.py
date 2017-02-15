from django.db import models


class PlayerInfo(models.Model):
    number = models.IntegerField(default = 0)
    name = models.CharField(max_length = 20)
    position = models.CharField(max_length = 20)
    hand = models.CharField(max_length = 20)
    birth = models.CharField(max_length = 20)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name


class BetterStat(models.Model):
    name = models.CharField(max_length=20)
    player_info = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    all_bats = models.IntegerField(null=True)
    at_bats = models.IntegerField(null=True)
    runs_scored = models.IntegerField(null=True)
    hits = models.IntegerField(null=True)
    doubles = models.IntegerField(null=True)
    triples = models.IntegerField(null=True)
    home_runs = models.IntegerField(null=True)
    total_base = models.IntegerField(null=True)
    runs_batted_in = models.IntegerField(null=True)
    stolen_bases = models.IntegerField(null=True)
    caught_stealing = models.IntegerField(null=True)
    bases_on_balls = models.IntegerField(null=True)
    hit_by_pitch = models.IntegerField(null=True)
    intentional_bob = models.IntegerField(null=True)
    strike_out = models.IntegerField(null=True)
    double_play = models.IntegerField(null=True)
    sacrifice = models.IntegerField(null=True)
    sacrifice_fly = models.IntegerField(null=True)
    batting_avg = models.FloatField(null=True)
    on_base_per = models.FloatField(null=True)
    slugging_per = models.FloatField(null=True)
    ops = models.FloatField(null=True)
    woba = models.FloatField(null=True)
    wrc_plus = models.FloatField(null=True)
    war = models.FloatField(null=True)
    wpa = models.FloatField(null=True)

    def __str__(self):
        return self.name


class PitcherStat(models.Model):
    name = models.CharField(max_length=20)
    player_info = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    game = models.IntegerField(null=True)
    complited_game = models.IntegerField(null=True)
    shutout = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    loses = models.IntegerField(null=True)
    saves = models.IntegerField(null=True)
    holds = models.IntegerField(null=True)
    innings = models.FloatField(null=True)
    runs = models.IntegerField(null=True)
    earned_runs = models.IntegerField(null=True)
    batter = models.IntegerField(null=True)
    hits = models.IntegerField(null=True)
    doubles = models.IntegerField(null=True)
    triples = models.IntegerField(null=True)
    home_runs = models.IntegerField(null=True)
    bases_on_balls = models.IntegerField(null=True)
    intentional_bob = models.IntegerField(null=True)
    hit_by_pitch = models.IntegerField(null=True)
    strike_out = models.IntegerField(null=True)
    balks = models.IntegerField(null=True)
    wild_pitches = models.IntegerField(null=True)
    era = models.FloatField(null=True)
    fip = models.FloatField(null=True)
    whip = models.FloatField(null=True)
    era_plus = models.FloatField(null=True)
    fip_plus = models.FloatField(null=True)
    war = models.FloatField(null=True)
    wpa = models.FloatField(null=True)

    def __str__(self):
        return self.name
