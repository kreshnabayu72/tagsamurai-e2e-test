---
id: TC-GS-HHR-E2E-038-last-scanned-dari-usage-event-produk-lain
title: "Last Scanned, Last Scanned In, Last User, dan Tab Usage Diperbarui dari Sesi Audit Fixed Asset dan Pair TAG Global Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-185
  - TC-GS-HHR-186
coverage:
  web: automated
---

# Last Scanned, Last Scanned In, Last User, dan Tab Usage Diperbarui dari Sesi Audit Fixed Asset dan Pair TAG Global Settings

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai simulator reader USB, mengubah Last Scanned dan Usage Event dua reader, dan membuat sesi audit Fixed Asset yang ditutup; tidak berjalan bersamaan dengan spec lain pada Client A.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader (Client A) untuk akun aktor pertama; layar dibuka lagi lewat langkah eksplisit sesudah ganti akun.
- Akun yang dipakai:

  | Akun | Email | Env var password | Dipakai di |
  |---|---|---|---|
  | Total Control (Sari Dewi), Client A | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` | Aktor default suite (login di hook `before`); membaca Handheld Reader dan melakukan Pair TAG (TC-GS-HHR-186) |
  | Budi Santoso, Client A | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `Spectra.env.GS_BUDI_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`) | Menutup sesi audit Fixed Asset (TC-GS-HHR-185) |

  Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Data Dinamis: Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. TC-GS-HHR-185 memakai DD-04 (`Gudang Reader - 2`, Serial Number `SN-HHR-00104`, belum pernah dipindai, tanpa Usage Event). TC-GS-HHR-186 memakai DD-07 (`Honeywell CK65 - 1`, Serial Number `SN-HHR-00108`, belum pernah dipindai, tanpa Usage Event) sebagai pengganti DD-04 supaya Tab Usage reader yang diasersi hanya memuat satu event dari aksi blok itu (lihat Notes). Seed bernama literal tanpa suffix karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g); baris diidentifikasi lewat Serial Number.
- Data pendukung (disediakan tim FE; mekanisme seeding tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA): satu sesi audit Fixed Asset Client A yang siap dipindai dengan reader DD-04 dan siap ditutup oleh Budi Santoso, dengan sedikitnya dua tag yang dapat dipindai; satu user uji Global Settings milik spec ini (`Fixture.hardwareHandheldReader.pairTagUser038`) beserta tag yang dapat dipasangkan lewat Pair TAG. Nomor task audit (Transaction ID) dicatat pada langkah 6.
- Cleanup: Seed Reader A dipulihkan ke kondisi awal oleh fixture backend sebelum spec (hook `before`) dan sesudah spec (hook `after`). Sesi audit, user uji, dan pasangan TAG yang dibuat spec dibersihkan di hook `after`; mekanisme pembersihan disediakan tim FE/BE. Kolom `Last Scanned In` dan `Last User` yang diaktifkan pada langkah 10 dipulihkan lewat Setup Column default di hook `after`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (kelas d, harness eksternal): simulator reader USB dan driver lokal yang dapat menghadirkan reader dengan Serial Number tertentu (`SN-HHR-00104` dan `SN-HHR-00108`) ke Fixed Asset > Audit dan ke Sync Panel Global Settings; mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD; ganti akun (logout lalu login); membaca jam klien yang sinkron dengan jam server (toleransi satu menit).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite), Last Scanned dan Usage Event DD-04 dan DD-07 (dipulihkan seperti di atas), kolom yang diaktifkan pada Column Visibility, dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### TC-GS-HHR-185: Sesi audit Fixed Asset ditutup dengan reader DD-04

1. Logout dari akun Total Control
2. Login sebagai Budi Santoso dengan `Spectra.env.GS_BUDI_PASSWORD`
3. Buka Fixed Asset > Audit, buka sesi audit yang disiapkan untuk reader DD-04
4. Pindai tag pertama memakai reader DD-04 (simulator USB)
5. Pindai tag kedua memakai reader DD-04 (simulator USB)
6. Tutup sesi audit, tunggu aksi selesai, lalu catat waktu sesudah penutupan (jam klien) dan nomor task audit
7. Logout dari akun Budi Santoso
8. Login sebagai Total Control (Sari Dewi) dengan `Spectra.env.GS_TC_PASSWORD`
9. Buka Global Settings > Hardware > Handheld Reader
10. Aktifkan kolom `Last Scanned In` dan `Last User` lewat Column Visibility
11. Verifikasi `Last Scanned` baris DD-04 (`Gudang Reader - 2`) terisi waktu penutupan sesi (toleransi satu menit dari waktu yang dicatat pada langkah 6)
12. Verifikasi `Last Scanned In` baris DD-04 menampilkan `Fixed Asset`
13. Verifikasi `Last User` baris DD-04 menampilkan `Budi S`
14. Klik `Device Name` baris DD-04 (`Gudang Reader - 2`)
15. Verifikasi tab `Usage` memuat tepat satu baris
16. Verifikasi baris tersebut berisi Product `Fixed Asset`, Event Type `Audit Scan`, `Transaction ID` sama dengan nomor task audit yang dicatat pada langkah 6, dan PIC `Budi S`
17. Klik `[✕]`

### TC-GS-HHR-186: Pair TAG di Global Settings mencatat event Global Settings

18. Buka Global Settings > User, lakukan Pair TAG pada user uji dengan memindai tag memakai reader DD-07 (`Honeywell CK65 - 1`, simulator USB; reader terdeteksi di Sync Panel Global Settings)
19. Buka Global Settings > Hardware > Handheld Reader
20. Klik `Device Name` baris DD-07 (`Honeywell CK65 - 1`)
21. Verifikasi tab `Usage` memuat satu baris dengan Product `Global Settings`, Event Type `Pair TAG`, dan `Transaction ID` `—`
22. Klik `[✕]`
23. Verifikasi `Last Scanned In` baris DD-07 menampilkan `Global Settings`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 185, 186. Spec ini kelas d (harness eksternal: simulator USB dan sesi audit produk lain) sehingga berdiri sendiri; hanya dua TC, keduanya berlabel `Manual Only (b)` di kolom Automation TC dan tetap dimasukkan (konvensi bagian 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 9 (ganti akun, sesi audit, pemindaian, penutupan, dan membuka layar), langkah 10 (mengaktifkan kolom yang diasersi), langkah 14 dan 20 (membuka Popup Detail), langkah 17 dan 22 (menutup popup), dan langkah 18 sampai 19 (aksi Pair TAG dan kembali ke layar Handheld Reader). Langkah 6 mencatat waktu sesudah penutupan dan nomor task audit sebagai pembanding (S-12).
- Perbedaan dari Data Uji TC: TC-GS-HHR-186 menyebut reader DD-04, sedangkan TC-GS-HHR-185 sudah menambahkan event Fixed Asset pada Tab Usage DD-04 (Expected TC-GS-HHR-186 menyatakan Tab Usage berisi satu baris `Global Settings`). Karena Seed Reader A tidak dipulihkan di antara dua TC dalam spec, TC-GS-HHR-186 memakai DD-07 yang juga belum pernah dipindai; objek uji (Pair TAG mencatat event Global Settings dan Last Scanned In) tidak berubah.
- Langkah 5 (tag kedua) ditambahkan karena Expected c TC-GS-HHR-185 ("satu event per sesi, bukan per tag") hanya bermakna bila lebih dari satu tag dipindai; TC hanya menulis "pindai tag".
- Pembagian TC lintas spec: TC-GS-HHR-187 dan 188 (asersi tidak ada Changelog, System Log, Activity Log, dan surface Usage Event reader terhapus) ada di spec 065; TC-GS-HHR-169 sampai 183 ada di spec 036 dan 037.
- Temuan untuk QA:
  - TC-GS-HHR-185 dan 186 memakai DD-04 (Seed Reader A, Status `Missing`) sebagai reader yang memindai; TC tidak menyatakan apakah reader berstatus `Missing` boleh dipakai memindai di Fixed Asset atau Global Settings. Spec mengikuti TC pada 185 dan memakai DD-07 (Available) pada 186; kebutuhan reader Missing pada 185 perlu dikonfirmasi.
  - TC-GS-HHR-185 mensyaratkan sesi audit Fixed Asset "siap ditutup oleh akun Budi Santoso" tetapi Budi Santoso tidak ada di Tabel Data Uji Pre-setup (aktor default Total Control adalah Sari Dewi), dan TC tidak menyebut cara menyiapkan sesi audit, tag, atau user Pair TAG; spec menuliskan ketiganya sebagai data yang disediakan tim FE tanpa mengarang endpoint (S-13). Spec memakai Budi Santoso hanya untuk menutup sesi dan Sari Dewi untuk membaca layar.
  - TC-GS-HHR-185 Expected a ("`Last Scanned` terisi waktu penutupan sesi") tidak menyebut format; spec membandingkan waktu dengan jam klien yang dicatat sesudah penutupan (toleransi satu menit), format tanggal mengikuti General Settings Client A.
  - TC-GS-HHR-186 Precondition d ("Reader DD-04 terdeteksi di Sync Panel Global Settings") tidak menyebut mekanisme simulasi reader; kemampuannya ditulis di Prerequisites tanpa mengarang endpoint.
  - Pemilihan tag dan user pada Pair TAG (TC-GS-HHR-186 langkah 1) tidak dirinci di TC; spec memakai user uji milik spec dan tag yang disediakan tim FE.
  - Mekanisme pemulihan Seed Reader A oleh fixture backend ("Reset antar TC" pada Catatan TC) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - Tidak ada Post Condition pada TC sumber spec ini.
