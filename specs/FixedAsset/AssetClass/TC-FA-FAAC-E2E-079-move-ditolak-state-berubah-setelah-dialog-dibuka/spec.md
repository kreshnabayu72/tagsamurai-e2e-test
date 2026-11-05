---
id: TC-FA-FAAC-E2E-079-move-ditolak-state-berubah-setelah-dialog-dibuka
title: "Move Ditolak atau Dilewati saat State Berubah Setelah Dialog Dibuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-208
  - TC-FA-FAAC-209
  - TC-FA-FAAC-210
coverage:
  web: automated
---

# Move Ditolak atau Dilewati saat State Berubah Setelah Dialog Dibuka

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Pelaku kedua: sesi API aktor (login API password, token tidak dihitung sebagai sesi web; lihat `suite.md`); bukan konteks UI kedua.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke keadaan semula oleh fixture BE di hook `before` dan `after` dan di langkah penghubung): 'Heavy Equipment' (HEAVY-EQ) dengan "Crane Rental Unit" (0 aset aktif), "Hydraulic Breaker" (0 aset aktif), "Plate Compactor" (0 aset aktif), dan "Wheel Loader" (4 aset aktif); 'Machinery' (MACHINERY) Active tanpa Asset Name ter-assign pada blok TC-208 (sesuai Pre-setup TC-208); 'Vehicles' (VEHICLES) sebagai tujuan; 'Office Equipment (Legacy)' (OFFICE-OLD) berstatus Inactive (precondition TC, tidak diasersi). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; sesi API aktor untuk memindahkan Asset Name, mengubah status aset, dan menonaktifkan Asset Class; kemampuan baca BE untuk Asset Class asal Asset Name.
- State global: status Asset Class MACHINERY, status aset Wheel Loader, dan keanggotaan Asset Name berubah; dipulihkan di hook `after`.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"

### TC-FA-FAAC-208: Move ditolak saat Asset Class tujuan menjadi Inactive setelah dialog dibuka

3. Klik ikon ⋯ pada baris "Crane Rental Unit" lalu pilih "Move"
4. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
5. Nonaktifkan "Machinery" (tanpa Asset Name) lewat toggle Active di sesi API aktor hingga tersimpan
6. Klik [Move] pada sesi pertama
7. Verifikasi Dialog Blok tampil: Title "Asset Class Unavailable", Body "• MACHINERY – Machinery" dan "This asset class is inactive. Activate it first.", tombol [OK]
8. Verifikasi "Crane Rental Unit" tidak berpindah: tetap di HEAVY-EQ
9. Klik [OK]
10. Aktifkan kembali "Machinery" lewat fixture BE

### TC-FA-FAAC-209: Move melewati Asset Name yang sudah dipindahkan pengguna lain

11. Centang baris "Hydraulic Breaker" dan "Plate Compactor", klik "Bulk Action", lalu pilih "Move to another asset class"
12. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
13. Pindahkan "Hydraulic Breaker" ke "Vehicles" lewat sesi API aktor hingga tersimpan
14. Catat jumlah entri Changelog Asset Class yang memuat "Hydraulic Breaker" (Nh) sebagai baseline lewat kemampuan baca log
15. Klik [Move] pada sesi pertama
16. Verifikasi "Hydraulic Breaker" dilewati dan tetap di Vehicles
17. Verifikasi "Plate Compactor" berpindah ke Machinery
18. Verifikasi muncul toast sukses: "Success, asset name has been moved."
19. Verifikasi jumlah entri Changelog Asset Class yang memuat "Hydraulic Breaker" sama dengan Nh (dilewati tanpa log)

### TC-FA-FAAC-210: Move ditolak tanpa toast saat status aset aktif berubah setelah dialog dibuka

20. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
21. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
22. Verifikasi Effective From dan pratinjau dampak tampil (aset aktif 4)
23. Ubah seluruh aset Wheel Loader menjadi tidak berlifecycle Active lewat sesi API aktor hingga tersimpan
24. Klik [Move] pada sesi pertama
25. Verifikasi [Move] ditolak tanpa perubahan data: "Wheel Loader" tetap di HEAVY-EQ
26. Verifikasi tidak ada toast
27. Verifikasi dialog Move tetap terbuka
28. Verifikasi Effective From dan pratinjau dampak Hidden (aset aktif 0)
29. Klik [Cancel]
30. Pulihkan status aset Wheel Loader menjadi Active lewat fixture BE
31. Kembali ke tabel Asset Class lewat Breadcrumb `Asset Class` (Detail tidak diubah)
32. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 208, 209, 210 (TC-208 mensyaratkan MACHINERY tanpa Asset Name sehingga dijalankan sebelum TC-209 memindahkan "Plate Compactor" ke MACHINERY).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class dan Asset Name seed dipakai apa adanya; dipulihkan oleh fixture BE.
- Pelaku kedua memakai sesi API (keputusan 2026-10-30): bukan kelas c, tanpa butir `P-2`; langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (S-03): langkah 1 (Search `HEAVY-EQ` untuk menemukan baris target karena tabel memuat lebih dari 25 baris, R-16), langkah 2 (membuka Detail HEAVY-EQ), 14 (baseline Changelog, S-12), 9 dan 29 (menutup dialog), 10 dan 30 (pemulihan state seed), langkah 31 dan 32 (kembali ke tabel dan mengosongkan Search di akhir).
- Langkah 22 menjadi anchor positif bagi asersi Hidden langkah 28 (tambahan terhadap TC, dicatat sesuai S-03).
- S-05 dan P-1: Expected "tanpa log" pada TC-209 diasersi di spec ini (langkah 19) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline yang dicatat sebelum aksi pemicu (S-12); aksinya bukan request langsung (kelas a), sehingga tidak masuk spec absence. TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class. Entri Move untuk "Plate Compactor" memang bertambah, sehingga baseline dan asersi dibatasi pada entri yang memuat Asset Name yang dilewati ("Hydraulic Breaker").
- Temuan untuk QA: Precondition TC-208 menyebut MACHINERY "tanpa Asset Name" sedangkan TC-190 mensyaratkan MACHINERY memiliki "Welding Machine"; spec memakai state yang disiapkan fixture BE per blok (disediakan tim FE/BE). TC-209 menyebut "tidak dihitung pada toast" padahal teks toast tidak memuat jumlah.
