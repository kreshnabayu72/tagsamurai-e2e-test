---
id: TC-FA-CAID-E2E-034-toggle-off-on-state-dan-lock
title: "Master Switch: OFF lalu ON, Form Dirty, Lock Selama Request, dan Dim Saat OFF"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-100
  - TC-FA-CAID-101
  - TC-FA-CAID-102
  - TC-FA-CAID-103
coverage:
  web: automated
---

# Master Switch: OFF lalu ON, Form Dirty, Lock Selama Request, dan Dim Saat OFF

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10) dan aset A1 sampai A5 (No 11) dipulihkan oleh hook `beforeEach` suite; baseline B2 (No 10: Separator Dash, Initial Company `ABC`, Division Code tercentang) disiapkan lewat seed API pada langkah pertama TC-FA-CAID-100. Aset yang diperiksa: A1 `JKT/LAP/T490/0926/1`, A2 `JKT/LAP/T490/0926/2`, A3 `JKT/LAP/T490/0000/3`.
- Alat uji (Pre-setup No 26): penahan respons request Toggle (delay jaringan) pada TC-FA-CAID-102; penahan dilepas segera setelah asersi lock selesai. Kemampuan mengamati jumlah request Toggle yang terkirim (pengamatan jaringan) disediakan tim FE.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); konfirmasi otomatis dialog `beforeunload` tidak dibutuhkan karena form ditutup lewat dialog `Unsaved Changes`.
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Master Switch menjadi OFF pada akhir spec (state TC-FA-CAID-103) dan konfigurasi sempat B2. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-100: Switch OFF lalu ON mempertahankan konfigurasi terakhir

1. Atur konfigurasi Company Alpha ke baseline B2 (seed API), lalu muat ulang halaman
2. Geser Master Switch ke OFF
3. Klik `[Disable]`
4. Geser Master Switch ke ON
5. Verifikasi Separator `- (Dash)` tetap tersimpan
6. Verifikasi Initial Company tercentang berisi `ABC`
7. Verifikasi Division Code tercentang tetap tersimpan
8. Verifikasi Live Preview menampilkan `ABC-JKT-LAP-T490-0000-0926-1`
9. Buka Fixed Asset > Assets > All Assets
10. Verifikasi A1 menjadi `ABC-JKT-LAP-T490-HR-0926-1`, A2 menjadi `ABC-JKT-LAP-T490-HR-0926-2`, A3 menjadi `ABC-JKT-LAP-T490-0000-0000-3` dengan nomor Increment 1, 2, 3 tidak berubah

### TC-FA-CAID-101: Toggle tidak mengirim perubahan form yang belum disimpan

11. Atur konfigurasi Company Alpha ke baseline B1 (seed API), lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID
12. Pilih Separator `- (Dash)` tanpa menekan `[Save]`
13. Geser Master Switch ke OFF
14. Klik `[Disable]`
15. Verifikasi tombol `[Save]` disabled walau form dirty
16. Geser Master Switch ke ON
17. Verifikasi Separator masih menampilkan `- (Dash)` sebagai perubahan belum disimpan
18. Verifikasi tombol `[Save]` aktif
19. Klik menu `Assets` pada sidebar navigasi
20. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
21. Klik `[Leave]`
22. Buka Fixed Asset > Assets > All Assets
23. Verifikasi Asset ID A1, A2, A3 setelah Toggle kembali `JKT/LAP/T490/0926/1`, `JKT/LAP/T490/0926/2`, `JKT/LAP/T490/0000/3` dengan Separator tersimpan Slash karena perubahan form tidak ikut terkirim

### TC-FA-CAID-102: Master Switch terkunci selama request Toggle berjalan

24. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
25. Tunda respons Toggle (delay jaringan)
26. Geser Master Switch ke OFF
27. Klik `[Disable]`
28. Klik Master Switch lagi selama respons ditunda
29. Verifikasi Master Switch terkunci selama respons ditunda
30. Verifikasi klik tambahan tidak mengirim request kedua
31. Lepas tahanan respons dan tunggu respons tiba
32. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil

### TC-FA-CAID-103: Saat OFF seluruh kontrol form di-dim dan disabled

33. Klik checkbox `Group Code`
34. Klik dropdown `Separator *`
35. Seret drag handle baris `Group Code`
36. Verifikasi checkbox, dropdown Separator, drag handle, dan input Initial Company tidak merespons karena disabled
37. Verifikasi Live Preview redup menampilkan `1`
38. Verifikasi tombol `[Save]` disabled

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 38 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik dan satu kelas harness (perilaku Master Switch pada konfigurasi Company Alpha), tanpa kelas lain; memisahkannya hanya menambah login, hook, dan pembukaan halaman yang sama. Tiap blok TC dimulai dari keadaan yang ditulis eksplisit (seed B2, seed B1, atau state OFF hasil blok sebelumnya).
- Langkah penghubung: langkah 1 dan 11 (seed baseline), langkah 9, 22, dan 24 (membuka halaman tujuan), langkah 19 sampai 21 (menutup form dirty lewat sidebar, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]`, S-08).
- TC-FA-CAID-103 mengandalkan state Master Switch OFF dengan Asset ID polos hasil Toggle TC-FA-CAID-102 (Pre-setup TC: baseline B1 dengan Master Switch OFF dan A1 sampai A3 `1`, `2`, `3`); keadaan yang sama dengan precondition TC.
- Penahanan respons pada TC-FA-CAID-102 hanya untuk mengamati lock (spinner/lock), bukan kelas b.
- Pembagian TC lintas spec: TC-FA-CAID-94 sampai 98 ada di spec 033.
- Temuan untuk QA:
  - TC-FA-CAID-101 Expected c menyebut "Separator tersimpan Slash"; spec mengasersi Asset ID berformat Slash sebagai bukti, karena TC tidak memberi langkah membuka Separator tersimpan.
  - TC-FA-CAID-103 Expected a menyebut "input Initial Company" tanpa langkah yang mengkliknya; spec mengasersinya dalam daftar elemen disabled tanpa aksi tambahan.
  - Post Condition TC-FA-CAID-100 sampai 103 tidak diasersi karena TC tidak memberi langkah observasinya.
