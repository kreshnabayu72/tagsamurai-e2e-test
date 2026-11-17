---
id: TC-FA-FAAC-E2E-076-move-batas-bawah-lanjutan-dan-versi-scheduled-tujuan
title: "Move: Batas Bawah Effective From Lanjutan dan Versi Scheduled Asset Class Tujuan"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-203
  - TC-FA-FAAC-204
  - TC-FA-FAAC-205
sourceRules: ["V-25", "F-FAAC-09.k9", "D-14", "E-FAAC-42", "T-08", "FAAC-LOGIC-07k", "FAAC-LOGIC-07b"]
smoke: []
dependsOn: []
trace:
  "V-25": [8, 16]
  "F-FAAC-09.k9": 9
  "D-14": [15, 31]
  "E-FAAC-42": [18, 34]
  "T-08": [19, 35]
  "FAAC-LOGIC-07k": [20, 23]
  "FAAC-LOGIC-07b": 32
coverage:
  web: automated
---

# Move: Batas Bawah Effective From Lanjutan dan Versi Scheduled Asset Class Tujuan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Class Active 'Heavy Equipment' (HEAVY-EQ) dengan Asset Name "Wheel Loader" (4 aset aktif); Asset Class Active 'Machinery' (MACHINERY) sebagai tujuan; 'Vehicles' (VEHICLES) berstatus Active tersedia sebagai tujuan; 'Office Equipment (Legacy)' (OFFICE-OLD) berstatus Inactive (precondition TC, tidak diasersi). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE untuk mengatur per blok Last Posted Period dan versi Scheduled MACHINERY (langkah 3, 11, 24, 27) dan memulihkannya di hook `after`; fixture BE untuk memulihkan "Wheel Loader" ke HEAVY-EQ (langkah 24); jam: bulan berjalan (M) dihitung pada zona waktu General Settings client (NC-11); kemampuan baca BE untuk Asset Class asal Asset Name.
- State global: Last Posted Period, versi Scheduled MACHINERY, dan keanggotaan "Wheel Loader" berubah; dipulihkan di hook `after`.
- Data uji per blok: TC-204 MACHINERY Last Posted Period = bulan berjalan M, Effective From = M, batas bawah M+1 (mis. Nov 2026); TC-203 MACHINERY Last Posted Period M-3, batas bawah M-2, Effective From = M-2 (mis. Aug 2026); TC-205 MACHINERY satu versi Scheduled dengan Effective From M+2 dan versi berlaku terakhir M-6, Effective From = M.
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (seed spec lain ikut tampil), sehingga Class Code target dijangkau lewat Search kode (R-16), bukan lewat posisi baris di halaman 1.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"

### TC-FA-FAAC-204: Seluruh bulan yang dapat dipilih ditolak bila batas bawah lebih lambat dari bulan berjalan

3. Atur MACHINERY memiliki Last Posted Period = bulan berjalan M lewat fixture BE
4. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
5. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
6. Pilih Effective From = bulan berjalan M
7. Klik [Move]
8. Verifikasi caption error: "Effective from must not be earlier than [MMM YYYY]" dengan [MMM YYYY] = bulan setelah bulan berjalan (mis. "Nov 2026")
9. Verifikasi Move belum dapat dilakukan sampai bulan batas bawah tiba: "Wheel Loader" tidak berpindah dan tetap di HEAVY-EQ
10. Klik [Cancel]

### TC-FA-FAAC-203: Effective From tepat di batas bawah diterima

11. Atur MACHINERY memiliki Last Posted Period M-3 (batas bawah M-2) lewat fixture BE
12. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
13. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
14. Pilih Effective From = bulan M-2
15. Verifikasi field Effective From menampilkan bulan M-2 yang dipilih
16. Verifikasi tidak ada caption error pada Effective From
17. Klik [Move]
18. Verifikasi dialog menutup
19. Verifikasi muncul toast sukses: "Success, asset name has been moved."
20. Verifikasi "Wheel Loader" tidak lagi tampil di tab Asset Names HEAVY-EQ
21. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `MACHINERY`, tekan Enter
22. Klik link Class Code "MACHINERY", lalu klik tab "Asset Names"
23. Verifikasi "Wheel Loader" tampil di tab Asset Names Machinery

### TC-FA-FAAC-205: Versi Scheduled pada Asset Class tujuan tidak menjadi batas bawah Effective From Move

24. Pulihkan "Wheel Loader" ke HEAVY-EQ lewat fixture BE
25. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
26. Klik link Class Code "HEAVY-EQ", lalu klik tab "Asset Names"
27. Atur MACHINERY memiliki satu versi Scheduled dengan Effective From M+2 dan versi berlaku terakhir M-6, tanpa Last Posted Period, lewat fixture BE
28. Klik ikon ⋯ pada baris "Wheel Loader" lalu pilih "Move"
29. Pilih "Destination Asset Class" = "MACHINERY – Machinery"
30. Pilih Effective From = bulan berjalan M
31. Verifikasi field Effective From menampilkan bulan berjalan M yang dipilih
32. Verifikasi tidak ada caption "Effective from must not be earlier than ..."
33. Klik [Move]
34. Verifikasi dialog menutup
35. Verifikasi muncul toast sukses: "Success, asset name has been moved."

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 204, 203, 205 (TC-204 ditolak lebih dulu; TC-203 dan TC-205 sama-sama memindahkan "Wheel Loader" sehingga langkah 24 memulihkannya di antaranya).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Class dan Asset Name seed dipakai apa adanya; dipulihkan oleh fixture BE.
- Langkah penghubung (S-03): langkah 1, 2, 3, 10, 11, 21, 22, 24, 25, 26, 27 (Search kode R-16, navigasi, pengaturan state periode/versi, pemulihan seed, menutup dialog).
- Langkah 16 dan 32: caption error diasersi absen sebelum [Move] diklik; anchor positifnya adalah langkah 15 dan 31 (field Effective From menampilkan bulan terpilih; bagian 8b butir 2).
- Temuan untuk QA: TC-204 menyebut "Move belum dapat dilakukan sampai bulan batas bawah tiba" tanpa langkah observasi tambahan; spec mengasersi Wheel Loader tetap di Asset Class asal.
