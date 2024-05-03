from player_presenter import PlayerPresenter
from player_view import PlayerView


class TestPlayer:

    def test_1(self):
        player_presenter = PlayerPresenter()
        player_presenter.bind(PlayerView())
        player_presenter.play()
        assert player_presenter.is_playing == True
        assert player_presenter.is_paused == False

    def test_2(self):
        player_presenter = PlayerPresenter()
        player_presenter.bind(PlayerView())
        player_presenter.play()
        player_presenter.play()
        assert player_presenter.is_playing == False
        assert player_presenter.is_paused == True

    def test_3(self):
        player_presenter = PlayerPresenter()
        player_presenter.bind(PlayerView())
        player_presenter.play()
        player_presenter.play()
        player_presenter.play()
        assert player_presenter.is_playing == True
        assert player_presenter.is_paused == False


