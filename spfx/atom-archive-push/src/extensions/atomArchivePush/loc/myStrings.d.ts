declare interface IAtomArchivePushCommandSetStrings {
  Title: string;
  PushButton: string;
  Cancel: string;
}

declare module 'AtomArchivePushCommandSetStrings' {
  const strings: IAtomArchivePushCommandSetStrings;
  export = strings;
}
