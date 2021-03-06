// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: modules/perception/lidar/app/proto/lidar_obstacle_tracking_config.proto
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Apollo.Perception.Lidar {

  /// <summary>Holder for reflection information generated from modules/perception/lidar/app/proto/lidar_obstacle_tracking_config.proto</summary>
  public static partial class LidarObstacleTrackingConfigReflection {

    #region Descriptor
    /// <summary>File descriptor for modules/perception/lidar/app/proto/lidar_obstacle_tracking_config.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static LidarObstacleTrackingConfigReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ckdtb2R1bGVzL3BlcmNlcHRpb24vbGlkYXIvYXBwL3Byb3RvL2xpZGFyX29i",
            "c3RhY2xlX3RyYWNraW5nX2NvbmZpZy5wcm90bxIXYXBvbGxvLnBlcmNlcHRp",
            "b24ubGlkYXIicAobTGlkYXJPYnN0YWNsZVRyYWNraW5nQ29uZmlnEhwKFG11",
            "bHRpX3RhcmdldF90cmFja2VyGAEgASgJEhgKEGZyYW1lX2NsYXNzaWZpZXIY",
            "AiABKAkSGQoRZnVzaW9uX2NsYXNzaWZpZXIYAyABKAliBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Apollo.Perception.Lidar.LidarObstacleTrackingConfig), global::Apollo.Perception.Lidar.LidarObstacleTrackingConfig.Parser, new[]{ "MultiTargetTracker", "FrameClassifier", "FusionClassifier" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class LidarObstacleTrackingConfig : pb::IMessage<LidarObstacleTrackingConfig> {
    private static readonly pb::MessageParser<LidarObstacleTrackingConfig> _parser = new pb::MessageParser<LidarObstacleTrackingConfig>(() => new LidarObstacleTrackingConfig());
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<LidarObstacleTrackingConfig> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Apollo.Perception.Lidar.LidarObstacleTrackingConfigReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LidarObstacleTrackingConfig() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LidarObstacleTrackingConfig(LidarObstacleTrackingConfig other) : this() {
      multiTargetTracker_ = other.multiTargetTracker_;
      frameClassifier_ = other.frameClassifier_;
      fusionClassifier_ = other.fusionClassifier_;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LidarObstacleTrackingConfig Clone() {
      return new LidarObstacleTrackingConfig(this);
    }

    /// <summary>Field number for the "multi_target_tracker" field.</summary>
    public const int MultiTargetTrackerFieldNumber = 1;
    private string multiTargetTracker_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string MultiTargetTracker {
      get { return multiTargetTracker_; }
      set {
        multiTargetTracker_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "frame_classifier" field.</summary>
    public const int FrameClassifierFieldNumber = 2;
    private string frameClassifier_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string FrameClassifier {
      get { return frameClassifier_; }
      set {
        frameClassifier_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "fusion_classifier" field.</summary>
    public const int FusionClassifierFieldNumber = 3;
    private string fusionClassifier_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string FusionClassifier {
      get { return fusionClassifier_; }
      set {
        fusionClassifier_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as LidarObstacleTrackingConfig);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(LidarObstacleTrackingConfig other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (MultiTargetTracker != other.MultiTargetTracker) return false;
      if (FrameClassifier != other.FrameClassifier) return false;
      if (FusionClassifier != other.FusionClassifier) return false;
      return true;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (MultiTargetTracker.Length != 0) hash ^= MultiTargetTracker.GetHashCode();
      if (FrameClassifier.Length != 0) hash ^= FrameClassifier.GetHashCode();
      if (FusionClassifier.Length != 0) hash ^= FusionClassifier.GetHashCode();
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (MultiTargetTracker.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(MultiTargetTracker);
      }
      if (FrameClassifier.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(FrameClassifier);
      }
      if (FusionClassifier.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(FusionClassifier);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (MultiTargetTracker.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(MultiTargetTracker);
      }
      if (FrameClassifier.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(FrameClassifier);
      }
      if (FusionClassifier.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(FusionClassifier);
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(LidarObstacleTrackingConfig other) {
      if (other == null) {
        return;
      }
      if (other.MultiTargetTracker.Length != 0) {
        MultiTargetTracker = other.MultiTargetTracker;
      }
      if (other.FrameClassifier.Length != 0) {
        FrameClassifier = other.FrameClassifier;
      }
      if (other.FusionClassifier.Length != 0) {
        FusionClassifier = other.FusionClassifier;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            input.SkipLastField();
            break;
          case 10: {
            MultiTargetTracker = input.ReadString();
            break;
          }
          case 18: {
            FrameClassifier = input.ReadString();
            break;
          }
          case 26: {
            FusionClassifier = input.ReadString();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code
