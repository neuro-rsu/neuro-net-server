from my_module import s
import sys
# from darts.models.forecasting.torch_forecasting_model import PastCovariatesTorchModel
from darts.utils.torch import MonteCarloDropout
from darts.logging import get_logger

logger = get_logger(__name__)

sys.stdout.write('All Ok!')

logger.info(f"111")
print(s)
