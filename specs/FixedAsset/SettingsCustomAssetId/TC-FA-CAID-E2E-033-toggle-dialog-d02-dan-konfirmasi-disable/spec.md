---
id: TC-FA-CAID-E2E-033-toggle-dialog-d02-dan-konfirmasi-disable
title: "Master Switch: Dialog D-02, Cancel, Esc, Backdrop, dan Konfirmasi Disable"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-94
  - TC-FA-CAID-95
  - TC-FA-CAID-96
  - TC-FA-CAID-97
  - TC-FA-CAID-98
coverage:
  web: automated
---

# Master Switch: Dialog D-02, Cancel, Esc, Backdrop, dan Konfirmasi Disable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11), dipulihkan oleh hook `beforeEach` suite. Aset yang diperiksa: A1 `JKT/LAP/T490/0926/1`, A2 `JKT/LAP/T490/0926/2`, A3 `JKT/LAP/T490/0000/3`, A4 (Disposed) `JKT/LAP/T490/0926/4`.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan membaca total entri Modal Changelog: Custom Asset ID sebelum aksi (disediakan tim FE/BE, N tidak diturunkan dari seeding karena audit trail permanen); kemampuan mengamati request Toggle yang terkirim (pemantauan jaringan pada sesi otomasi, Pre-setup No 26 TC; kemampuan disediakan tim FE).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Master Switch menjadi OFF dan Asset ID A1 sampai A3 menjadi nomor Increment polos pada TC-FA-CAID-98. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Modal Changelog: Custom Asset ID, catat total entri sebagai baseline, lalu tutup modal

### TC-FA-CAID-94: Dialog D-02 saat Master Switch digeser ke OFF

2. Geser Master Switch ke OFF
3. Verifikasi dialog berjudul `Disable Custom Asset ID` dengan severity warning tampil
4. Verifikasi body dialog berbunyi `Disabling Custom Asset ID will revert all existing assets to the plain system-generated Increment format. This action cannot be undone automatically.` disusul `Are you sure you want to disable it?`
5. Verifikasi footer dialog memuat tombol `[Cancel]` (text, contrast) dan `[Disable]` (filled, danger)
6. Verifikasi belum ada request Toggle terkirim
7. Verifikasi Master Switch berada di posisi OFF yang baru digeser selama dialog terbuka

### TC-FA-CAID-97: Klik backdrop tidak menutup dialog D-02

8. Klik area backdrop di luar dialog
9. Verifikasi dialog `Disable Custom Asset ID` tetap terbuka
10. Verifikasi Master Switch tetap di posisi OFF yang baru digeser

### TC-FA-CAID-96: Tombol Esc setara Cancel

11. Tekan `Esc`
12. Verifikasi dialog tertutup
13. Verifikasi Master Switch kembali ke posisi ON
14. Verifikasi tidak ada request Toggle terkirim
15. Verifikasi tidak ada toast

### TC-FA-CAID-95: Cancel pada dialog D-02

16. Geser Master Switch ke OFF
17. Klik `[Cancel]` pada dialog
18. Verifikasi dialog tertutup
19. Verifikasi Master Switch kembali ke posisi ON
20. Verifikasi tidak ada toast
21. Buka Fixed Asset > Assets > All Assets
22. Verifikasi Asset ID A1 tidak berubah (`JKT/LAP/T490/0926/1`)
23. Verifikasi Asset ID A2 tidak berubah (`JKT/LAP/T490/0926/2`)
24. Verifikasi Asset ID A3 tidak berubah (`JKT/LAP/T490/0000/3`)
25. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu buka Modal Changelog: Custom Asset ID
26. Verifikasi total entri Modal Changelog: Custom Asset ID sama dengan baseline sehingga tidak memuat entri Status baru
27. Tutup Modal Changelog: Custom Asset ID

### TC-FA-CAID-98: Konfirmasi Disable

28. Geser Master Switch ke OFF
29. Klik `[Disable]`
30. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
31. Verifikasi Master Switch berada pada posisi OFF
32. Verifikasi kontrol form di-dim dan disabled
33. Verifikasi Live Preview menampilkan `1`
34. Verifikasi tombol `[Save]` disabled
35. Buka Fixed Asset > Assets > All Assets
36. Verifikasi A1 menjadi `1` tanpa padding nol dan tanpa pemisah
37. Verifikasi A2 menjadi `2` tanpa padding nol dan tanpa pemisah
38. Verifikasi A3 menjadi `3` tanpa padding nol dan tanpa pemisah
39. Verifikasi A4 (Disposed) tetap `JKT/LAP/T490/0926/4`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 39 langkah tanpa langkah bersyarat, melewati sekitar 35 langkah. Alasan: semua blok satu kelas (fungsional dialog D-02 Master Switch), satu akun dan satu layar, TC-FA-CAID-95 dan TC-FA-CAID-98 membuka dialog sendiri sehingga berdiri sendiri, dan kelebihan langkah berasal dari pemecahan Asset ID per aset (S-01), bukan dari TC tambahan.
- Langkah penghubung: langkah 1 (mencatat baseline total entri Changelog, S-12), langkah 21, 25, dan 35 (membuka halaman tujuan), langkah 27 (menutup modal).
- Urutan TC di spec: TC-FA-CAID-94, TC-FA-CAID-97, TC-FA-CAID-96, TC-FA-CAID-95, TC-FA-CAID-98. Dialog D-02 yang dibuka pada langkah 2 (TC-FA-CAID-94) dipakai ulang oleh TC-FA-CAID-97 dan TC-FA-CAID-96 karena aksi pembuka mereka identik (geser Master Switch ke OFF); TC-FA-CAID-95 dan TC-FA-CAID-98 membuka dialog sendiri. Aksi yang mengubah data (`[Disable]`) berada di akhir.
- Pemulihan Master Switch ke ON dilakukan hook `after` suite (R-08); form tidak dirty di akhir spec.
- S-01: Asset ID tiap aset (A1, A2, A3) diasersi dengan satu `Verifikasi` per aset (langkah 22 sampai 24 dan 36 sampai 38). Judul dan severity, body, dan pasangan tombol footer dialog (langkah 3 sampai 5) mengikuti pengelompokan butir Expected TC-FA-CAID-94 a sampai c.
- Asersi "tidak memuat entri Status baru" pada langkah 26 memakai baseline total entri (S-12, bukan kelas g) dan berjangkar pada Modal Changelog yang terbuka dengan total terbaca.
- Temuan untuk QA:
  - TC-FA-CAID-95 Expected a menyebut "tidak ada toast" tanpa jendela waktu; diasersi segera setelah dialog tertutup.
  - Post Condition TC-FA-CAID-94 sampai 98 tidak diasersi karena TC tidak memberi langkah observasinya.
