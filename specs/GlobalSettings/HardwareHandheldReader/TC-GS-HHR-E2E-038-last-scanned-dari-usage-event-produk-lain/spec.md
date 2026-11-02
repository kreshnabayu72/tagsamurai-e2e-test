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
- Layar awal: akun aktor pertama spec adalah Total Control (Sari Dewi) (login di hook `before`); hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader sehingga langkah 1 langsung membuka Popup Detail untuk membaca baseline. Fixed Asset > Audit dibuka lewat langkah 5 sesudah ganti akun ke Budi Santoso (langkah 3 dan 4); layar Handheld Reader dibuka lagi lewat langkah 11 sesudah ganti akun kembali ke Total Control (langkah 9 dan 10).
- Akun yang dipakai:

  | Akun | Email | Env var password | Dipakai di |
  |---|---|---|---|
  | Total Control (Sari Dewi), Client A | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` | Akun aktor pertama spec (login di hook `before`); membaca baseline Tab Usage (langkah 1, 2, 21, dan 22), login kembali lewat langkah ganti akun eksplisit (langkah 10) untuk membaca Handheld Reader, dan melakukan Pair TAG (TC-GS-HHR-186); hook `after` mengembalikan sesi ke akun ini |
  | Budi Santoso, Client A | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE | `Spectra.env.GS_BUDI_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`) | Login lewat langkah ganti akun eksplisit (langkah 4); menutup sesi audit Fixed Asset (TC-GS-HHR-185) |

  Password tidak ditulis di spec atau fixture.
- Data Dinamis (Seed Reader A, dipulihkan fixture backend): Seed Reader A (DD-01 sampai DD-10; fixture baru `Fixture.hardwareHandheldReader.seedReaderA`), format tanggal default Client A `dd/MM/yy` 24-hour. TC-GS-HHR-185 memakai DD-04 (`Gudang Reader - 2`, Serial Number `SN-HHR-00104`, belum pernah dipindai, tanpa Usage Event). TC-GS-HHR-186 memakai DD-07 (`Honeywell CK65 - 1`, Serial Number `SN-HHR-00108`, belum pernah dipindai, tanpa Usage Event) sebagai pengganti DD-04 supaya Tab Usage reader yang diasersi hanya bertambah dengan event dari aksi blok itu (lihat Notes). Seed bernama literal tanpa suffix karena Device Name bawaan ditentukan sistem (HHR-LOGIC-02g); baris diidentifikasi lewat Serial Number.
- Data pendukung (disediakan tim FE; mekanisme seeding tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA): satu sesi audit Fixed Asset Client A yang siap dipindai dengan reader DD-04 dan siap ditutup oleh Budi Santoso, dengan sedikitnya dua tag yang dapat dipindai; satu user uji Global Settings milik spec ini (`Fixture.hardwareHandheldReader.pairTagUser038`) beserta tag yang dapat dipasangkan lewat Pair TAG. Nomor task audit (Transaction ID) dicatat pada langkah 8.
- Cleanup: Seed Reader A dipulihkan ke kondisi awal oleh fixture backend sebelum spec (hook `before`) dan sesudah spec (hook `after`); Tab Usage DD-04 dan DD-07 dikosongkan oleh reset tingkat reader di hook yang sama (lihat Kemampuan teknis). Sesi audit, user uji, dan pasangan TAG yang dibuat spec dibersihkan di hook `after`; mekanisme pembersihan disediakan tim FE/BE. Kolom `Last Scanned In` dan `Last User` yang diaktifkan pada langkah 12 dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (disediakan tim FE; spec ini terdaftar di `suite.md`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (kelas d, harness eksternal): simulator reader USB dan driver lokal yang dapat menghadirkan reader dengan Serial Number tertentu (`SN-HHR-00104` dan `SN-HHR-00108`) ke Fixed Asset > Audit dan ke Sync Panel Global Settings; mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD; ganti akun (logout lalu login); membaca jam klien yang sinkron dengan jam server (toleransi satu menit); membaca jumlah baris tab `Usage` (baseline N0, S-12) lewat kemampuan baca yang disediakan tim FE/BE (8b butir 10); kemampuan reset tingkat reader yang mengosongkan Tab Usage DD-04 dan DD-07 di hook `before` dan `after` (disediakan tim FE/BE; hitungan sesudah aksi tetap selisih terhadap baseline N0); menghapus preferensi kolom di browser (disediakan tim FE).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite), Last Scanned dan Usage Event DD-04 dan DD-07 (dipulihkan seperti di atas), kolom yang diaktifkan pada Column Visibility, dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### TC-GS-HHR-185: Sesi audit Fixed Asset ditutup dengan reader DD-04

1. Klik `Device Name` baris DD-04 (`Gudang Reader - 2`)
2. Catat jumlah baris tab `Usage` DD-04 sebagai baseline N0 TC-GS-HHR-185, lalu klik `[✕]`
3. Logout dari akun Total Control (Sari Dewi)
4. Login sebagai Budi Santoso dengan `Spectra.env.GS_BUDI_PASSWORD`
5. Buka Fixed Asset > Audit, buka sesi audit yang disiapkan untuk reader DD-04
6. Pindai tag pertama memakai reader DD-04 (simulator USB)
7. Pindai tag kedua memakai reader DD-04 (simulator USB)
8. Tutup sesi audit, tunggu aksi selesai, lalu catat waktu sesudah penutupan (jam klien) dan nomor task audit
9. Logout dari akun Budi Santoso
10. Login sebagai Total Control (Sari Dewi) dengan `Spectra.env.GS_TC_PASSWORD`
11. Buka Global Settings > Hardware > Handheld Reader
12. Aktifkan kolom `Last Scanned In` dan `Last User` lewat Column Visibility
13. Verifikasi `Last Scanned` baris DD-04 (`Gudang Reader - 2`) terisi waktu penutupan sesi (toleransi satu menit dari waktu yang dicatat pada langkah 8)
14. Verifikasi `Last Scanned In` baris DD-04 menampilkan `Fixed Asset`
15. Verifikasi `Last User` baris DD-04 menampilkan `Budi S`
16. Klik `Device Name` baris DD-04 (`Gudang Reader - 2`)
17. Verifikasi jumlah baris tab `Usage` DD-04 bertambah tepat satu dibanding baseline N0 yang dicatat pada langkah 2
18. Verifikasi baris baru berisi Product `Fixed Asset`, Event Type `Audit Scan`, `Transaction ID` sama dengan nomor task audit yang dicatat pada langkah 8, dan PIC `Budi S`
19. Verifikasi event tercatat satu per sesi audit, bukan satu per tag (dua tag dipindai pada langkah 6 dan 7, tab `Usage` bertambah satu baris, bukan dua)
20. Klik `[✕]`

### TC-GS-HHR-186: Pair TAG di Global Settings mencatat event Global Settings

21. Klik `Device Name` baris DD-07 (`Honeywell CK65 - 1`)
22. Catat jumlah baris tab `Usage` DD-07 sebagai baseline N0 TC-GS-HHR-186, lalu klik `[✕]`
23. Buka Global Settings > User, lakukan Pair TAG pada user uji dengan memindai tag memakai reader DD-07 (`Honeywell CK65 - 1`, simulator USB; reader terdeteksi di Sync Panel Global Settings)
24. Tunggu aksi selesai (Pair TAG selesai)
25. Buka Global Settings > Hardware > Handheld Reader
26. Klik `Device Name` baris DD-07 (`Honeywell CK65 - 1`)
27. Verifikasi jumlah baris tab `Usage` DD-07 bertambah tepat satu dibanding baseline N0 yang dicatat pada langkah 22
28. Verifikasi baris baru berisi Product `Global Settings`, Event Type `Pair TAG`, dan `Transaction ID` `—`
29. Klik `[✕]`
30. Verifikasi `Last Scanned In` baris DD-07 menampilkan `Global Settings`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 185, 186. Spec ini kelas d (harness eksternal: simulator USB dan sesi audit produk lain) sehingga berdiri sendiri; hanya dua TC, keduanya berlabel `Manual Only (b)` di kolom Automation TC dan tetap dimasukkan (konvensi bagian 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 21 (membuka Popup Detail untuk baseline), langkah 2 dan 22 (mencatat baseline N0 lalu menutup popup), langkah 3 sampai 12 (ganti akun ke Budi Santoso, sesi audit, pemindaian, penutupan, ganti akun kembali, membuka layar, dan mengaktifkan kolom yang diasersi), langkah 16 dan 26 (membuka Popup Detail), langkah 20 dan 29 (menutup popup), langkah 23 (aksi Pair TAG), langkah 24 ("Tunggu aksi selesai" karena langkah berikutnya berpindah surface dan hasil Pair TAG tidak diasersi langsung), dan langkah 25 (kembali ke layar Handheld Reader). Langkah 8 mencatat waktu sesudah penutupan dan nomor task audit sebagai pembanding (S-12).
- Urutan akun: TC-GS-HHR-185 Langkah 1 membaca baseline Tab Usage sebagai Total Control sebelum sesi audit, sedangkan Langkah 2 TC (sesi audit) dijalankan Budi Santoso; spec memulai dengan Total Control (hook `before`), ganti akun ke Budi Santoso untuk sesi audit (langkah 3 dan 4), lalu kembali ke Total Control (langkah 9 dan 10).
- TC-GS-HHR-185 memakai DD-04 dan TC-GS-HHR-186 memakai DD-07 (keduanya belum pernah dipindai), sehingga kenaikan Tab Usage tiap reader hanya berasal dari aksi blok masing-masing. Hitungan Usage Event memakai selisih terhadap baseline N0 (S-12, TC-GS-HHR-185 dan 186 relatif); keadaan awal reader bersih dijamin reset tingkat reader di Prerequisites.
- Langkah 7 (tag kedua) ditambahkan karena Expected c TC-GS-HHR-185 ("satu event per sesi, bukan per tag") hanya bermakna bila lebih dari satu tag dipindai; TC hanya menulis "pindai tag".
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Pembagian TC lintas spec: TC-GS-HHR-187 dan 188 (asersi tidak ada Changelog, System Log, Activity Log, dan surface Usage Event reader terhapus) ada di spec 065; TC-GS-HHR-169 sampai 178 ada di spec 036, TC-GS-HHR-179 sampai 182 di spec 037, dan TC-GS-HHR-183 di spec 058.
- Temuan untuk QA:
  - TC-GS-HHR-185 memakai DD-04 (Seed Reader A, Status `Missing`) sebagai reader yang memindai; TC tidak menyatakan apakah reader berstatus `Missing` boleh dipakai memindai di Fixed Asset. Spec mengikuti TC; kebutuhan reader Missing perlu dikonfirmasi.
  - TC-GS-HHR-185 mensyaratkan sesi audit Fixed Asset "siap ditutup oleh akun Budi Santoso" tetapi Budi Santoso tidak ada di Tabel Data Uji Pre-setup (aktor default Total Control adalah Sari Dewi), dan TC tidak menyebut cara menyiapkan sesi audit, tag, atau user Pair TAG; spec menuliskan ketiganya sebagai data yang disediakan tim FE tanpa mengarang endpoint (S-13). Spec memakai Budi Santoso hanya untuk menutup sesi dan Sari Dewi untuk membaca layar.
  - TC-GS-HHR-185 Expected a ("`Last Scanned` terisi waktu penutupan sesi") tidak menyebut format; spec membandingkan waktu dengan jam klien yang dicatat sesudah penutupan (toleransi satu menit), format tanggal mengikuti General Settings Client A.
  - TC-GS-HHR-186 Precondition d ("Reader DD-04 terdeteksi di Sync Panel Global Settings") tidak menyebut mekanisme simulasi reader; kemampuannya ditulis di Prerequisites tanpa mengarang endpoint.
  - Pemilihan tag dan user pada Pair TAG (TC-GS-HHR-186 langkah 1) tidak dirinci di TC; spec memakai user uji milik spec dan tag yang disediakan tim FE.
  - Tidak ada Post Condition pada TC sumber spec ini.
