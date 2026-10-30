---
id: TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps
title: "Pencocokan Real-Time GPS: Official, Damaged/Missing Tetap Official, Self-Purchased, Needs Info, Sudah Aktif, dan In Use Client Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-59
  - TC-GS-TAG-60
  - TC-GS-TAG-61
  - TC-GS-TAG-62
  - TC-GS-TAG-70
  - TC-GS-TAG-71
coverage:
  web: automated
---

# Pencocokan Real-Time GPS: Official, Damaged/Missing Tetap Official, Self-Purchased, Needs Info, Sudah Aktif, dan In Use Client Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor utama: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Stok resmi Admin Console Client A (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`) di-seed idempotent oleh fixture BE di hook `before`: GPS `356938035643001` (DD-S1) Available dan GPS `356938035643002` (DD-S2) Damaged/Missing. Akun Admin Console untuk seeding stok disediakan tim FE (S-13).
- Data identifier: `356938035643101` (DD-N1) tidak ada di stok resmi dan tidak ada di registri Client A; `356938035643501` (DD-09) sudah aktif di registri Client A (bagian Seed Registri A, dipakai sebagai precondition TC-70: "sudah aktif dari sesi sebelumnya", tidak diasersi di luar toast); `356938035643201` (DD-N4) In Use di Client B (Total Control Client B `totalControl_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_TC_PASSWORD`, pemilik unit; seeding unit In Use disediakan tim FE, tidak ada login Client B di spec ini).
- Opsi mandiri (BYO) aktif untuk Client A; Template Self-Purchased kosong pada awal tiap sesi Activate.
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE, S-13) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### Sesi 1 (Template kosong)

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`

### TC-GS-TAG-59: Stok resmi Available menjadi Official

2. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
3. Verifikasi baris `356938035643001` berstatus `Official`
4. Verifikasi baris `356938035643001` memuat Device Name `Teltonika FMB920` dari stok
5. Verifikasi baris `356938035643001` memuat SKU `SKU-GPS-01` dari stok
6. Verifikasi baris `356938035643001` memuat Brand `Teltonika` dari stok
7. Verifikasi baris `356938035643001` memuat Model/Type `FMB920` dari stok
8. Verifikasi aksi baris `356938035643001` hanya `Remove`
9. Verifikasi `Total Scanned: 1`

### TC-GS-TAG-60: Stok resmi Damaged/Missing tetap Official

10. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643002`
11. Verifikasi baris `356938035643002` berstatus `Official`

### TC-GS-TAG-62: Tidak di stok dengan Template kosong menjadi Needs Info

12. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` tanpa mengisi Template
13. Verifikasi baris `356938035643101` berstatus `Needs Info` dengan metadata `—`
14. Verifikasi aksi baris `356938035643101`: `Resolve` dan `Remove`
15. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog `Unsaved Changes` (staging berisi baris)

### Sesi 2 (Template terisi)

16. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
17. Buka section `Self-Purchased Template`
18. Isi Template Device Name `Queclink GV300`, Brand `Queclink`, Model/Type `GV300`

### TC-GS-TAG-70: Identifier yang sudah aktif di registri sendiri ditolak T-19

19. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643501`
20. Verifikasi toast error `Error, TAG is already activated.`
21. Verifikasi baris `356938035643501` tidak masuk tabel staging

### TC-GS-TAG-61: Tidak di stok dengan Template lengkap menjadi Self-Purchased

22. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101`
23. Verifikasi baris `356938035643101` berstatus `Self-Purchased`
24. Verifikasi baris `356938035643101` memuat Device Name `Queclink GV300`
25. Verifikasi baris `356938035643101` memuat SKU `—`
26. Verifikasi baris `356938035643101` memuat Brand `Queclink`
27. Verifikasi baris `356938035643101` memuat Model/Type `GV300`
28. Verifikasi aksi baris `356938035643101`: `Edit` dan `Remove`

### TC-GS-TAG-71: In Use di client lain tidak memunculkan lencana kolisi

29. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643201`
30. Hover lencana status baris `356938035643201`
31. Verifikasi baris `356938035643201` berlencana `Self-Purchased` (diperlakukan sama seperti tidak cocok)
32. Verifikasi tidak ada lencana atau tooltip kolisi pada baris `356938035643201`
33. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog `Unsaved Changes` (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (pencocokan real-time dengan entri manual GPS).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: sesi 1 memakai Template kosong (TC-59, TC-60, TC-62; TC-62 mensyaratkan Template kosong); sesi 2 memakai Template terisi (TC-70 sebagai kasus ditolak lebih dulu, lalu TC-61 dan TC-71). TC-61 dan TC-62 memakai identifier yang sama (`356938035643101`) sehingga tidak berada di satu sesi.
- Pembagian TC: TC-69 (pindai ulang RFID, T-02) ada di spec 025 karena memakai pemindai hardware (kelas d dipisah, bagian 3 prinsip 13); TC-63 dan TC-64 (Error T-10 dan T-11) ada di spec 023.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Buka section` dan `Isi Template` pada sesi 2 menjalankan Precondition TC-61/71 (Template terisi); langkah hover pada TC-71 menjalankan pengamatan tooltip yang tidak ada langkahnya di TC; `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03) karena dialog `Unsaved Changes` muncul pada sesi dengan baris staging, sedangkan definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-71 menyebut Template Device Name `Queclink GV300` dan Brand `Queclink` tanpa Model/Type; spec memakai Template sesi 2 (Model/Type `GV300` ikut terisi dari TC-61) sehingga baris `356938035643201` memuat Model/Type `GV300`, yang tidak diasersi.
  - TC-70 Pre-setup "sudah aktif di registri Client A dari sesi sebelumnya" tanpa menyebut identifier dari Seed Registri A; spec memakai DD-09 (`356938035643501`) yang memang Seed Registri A GPS Available.
  - TC-71: Client B sebagai pemilik unit In Use hanya fixture; tidak ada langkah di Client B.
