---
id: TC-FA-TDC-E2E-074-d-09-effective-from-kosong-cancel-dan-esc
title: "Dialog Save Changes D-09: Cancel dan Esc Menutup Tanpa Menyimpan, Effective From Kosong Ditolak dengan Caption V-19"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-262
  - TC-FA-TDC-265
  - TC-FA-TDC-266
coverage:
  web: automated
---

# Dialog Save Changes D-09: Cancel dan Esc Menutup Tanpa Menyimpan, Effective From Kosong Ditolak dengan Caption V-19

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Kemampuan teknis: pembacaan versi class lewat fixture BE (untuk asersi "tidak ada versi baru"; disediakan tim FE/BE) dan cara mengosongkan nilai Effective From lewat data basi pada langkah 21 (TC tidak menyebut mekanismenya; disediakan tim FE/BE, S-13).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`):

| TC | Class (Class Code bersuffix) | Keterangan |
|---|---|---|
| TC-262, 265, 266 | `KHS-V1-{runId}-074` | Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, Used By 0, satu versi Current tanpa Effective From, tanpa versi Scheduled |

- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `KHS-V1-{runId}-074`, tekan Enter
2. Klik link Class Code `KHS-V1-{runId}-074` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`

### TC-FA-TDC-265: Tombol Cancel pada D-09 kembali ke Drawer tanpa menyimpan

5. Klik `[Cancel]` pada dialog Save Changes
6. Verifikasi dialog Save Changes tertutup
7. Verifikasi Drawer Edit tetap terbuka
8. Verifikasi Useful Life `10` dipertahankan pada Drawer Edit
9. Verifikasi tidak ada toast
10. Verifikasi tidak ada versi baru: class `KHS-V1-{runId}-074` tetap satu versi (dibaca lewat fixture BE)

### TC-FA-TDC-266: Esc pada D-09 menutup dialog tanpa menyimpan

11. Klik `[Save]`
12. Tekan `Esc`
13. Verifikasi dialog Save Changes tertutup
14. Verifikasi Drawer Edit tetap terbuka
15. Verifikasi Useful Life `10` dipertahankan pada Drawer Edit
16. Verifikasi tidak ada versi baru: class `KHS-V1-{runId}-074` tetap satu versi (dibaca lewat fixture BE)
17. Verifikasi tidak ada toast

### TC-FA-TDC-262: Effective From kosong dari data basi ditolak saat Apply dengan caption V-19

18. Klik `[Save]`
19. Klik Select Effective From
20. Verifikasi daftar opsi Select Effective From hanya berisi tahun pajak dan tidak ada opsi kosong
21. Kosongkan nilai Effective From lewat data basi (Select tidak menyediakan opsi kosong)
22. Verifikasi placeholder `Select tax year` tampil pada Select Effective From
23. Klik `[Apply]`
24. Verifikasi caption `Effective from must not be empty` muncul pada Effective From
25. Verifikasi dialog Save Changes tetap terbuka
26. Verifikasi tidak ada versi baru: class `KHS-V1-{runId}-074` tetap satu versi (dibaca lewat fixture BE)
27. Klik `[Cancel]` pada dialog Save Changes
28. Klik `[×]` pada Drawer Edit
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`

## Notes

- Urutan TC dalam spec: 265, 266, 262 (TC yang berakhir dengan penolakan diletakkan paling akhir; S-10). Ketiga TC memakai satu class dan satu sesi Drawer Edit yang dibuka pada langkah 2 sampai 4; langkah 1 sampai 3 tiap TC identik dengan keadaan yang sudah terbentuk, dan dialog Save Changes dibuka ulang dengan `[Save]`.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 27 sampai 30 (menutup dialog dan Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- Absence pada langkah 9 dan 17 (toast): anchor positif adalah penutupan dialog dan Drawer yang tampil (langkah 6, 7, 13, 14). Absence pada langkah 20: anchor positif adalah daftar opsi yang terbuka (langkah 19).
- Temuan untuk QA:
  - TC-262: langkah 5 menyebut "data basi atau request langsung" tanpa memilih satu mekanisme. Bila yang dimaksud request langsung ke server, asersi caption `Effective from must not be empty` adalah perilaku FE dan tidak dapat diasersi pada jalur itu (bagian 8b butir 1); spec memakai jalur data basi lewat UI.
  - TC-262 memuat dua butir Precondition berlabel `d` (class `KHS-V1` dan "Select Effective From tidak menawarkan opsi kosong").
  - TC-265 dan TC-266 Post Condition "tidak ada entri log" dan "class tetap satu versi" tanpa langkah observasi TC; "tidak ada versi baru" diasersi lewat fixture BE karena ada di Expected, sedangkan "tidak ada entri log" tidak diasersi (S-01).
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-074` (S-12); batas panjang Class Code tidak tertulis di TC.
