import argparse
from train import train 
from utils import setup





if __name__ == '__main__':

  p = argparse.ArgumentParser()
  p.add_argument("--batch_size", type=int, default=32, help="batch_size")
  p.add_argument("--learning_rate", default=5e-5, help="learning_rate")
  p.add_argument("--optimizer", type=str, default='adam', help="['adam', 'sgd', 'rmsprop', 'adagrad'] 중 선택")
  p.add_argument("--epochs", type=int, default=3, help="epochs")
  p.add_argument("--run_name", type=str, default='wow_project', help='wandb, run_name')
  p.add_argument("--project_name", type=str, default='final_project', help='wandb, project_name')
  p.add_argument("--entity_name", type=str, default='ugiugi', help='wandb, entity_name')

  args = p.parse_args()
  setup()
  train(args)
  
  