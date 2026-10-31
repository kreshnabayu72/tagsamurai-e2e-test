---
id: TC-GS-GSET-E2E-019-navigasi-tanpa-dialog-unsaved-revert-beforeunload-dan-setelah-save
title: "Button Save dan Navigasi Tanpa Dialog Unsaved Changes: Tanpa Perubahan, Revert, Reload, dan Setelah Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-29
  - TC-GS-GSET-51
  - TC-GS-GSET-114
  - TC-GS-GSET-52
  - TC-GS-GSET-53
coverage:
  web: automated
---

# Button Save dan Navigasi Tanpa Dialog Unsaved Changes: Tanpa Perubahan, Revert, Reload, dan Setelah Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`). Save hanya terjadi di blok terakhir (langkah 22); hook `after` suite memulihkan baseline sesudahnya.
- Kemampuan teknis: menangani dialog konfirmasi bawaan browser `beforeunload` pada pemuatan ulang halaman (TC-GS-GSET-52 berstatus Manual Only di TC; harness mendeteksi dialog dan membatalkan reload sehingga halaman tetap terbuka), tanpa langkah bersyarat (S-08).
- Data Uji: Session Idle Timeout `1 hour` dan `30 minutes` (nilai tersimpan); tujuan navigasi in-app Global Settings > Activity Log (klik menu pada sidebar). Tidak ada Data Dinamis; baris Changelog dihasilkan oleh Save di langkah 22 dan tidak dihapus (audit trail permanen).
- Spec mengubah record Client A di blok terakhir sehingga suite berjalan serial (`parallel: false`, lihat `suite.md`).
- TC-GS-GSET-29, 51, 114, 52, 53: login sebagai Total Control dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-29: Button Save disabled, enabled saat berubah, disabled lagi saat dikembalikan

1. Verifikasi Button "Save" disabled dan tetap tampil saat form baru dimuat
2. Pilih Session Idle Timeout `1 hour`
3. Verifikasi Button "Save" enabled
4. Pilih kembali Session Idle Timeout `30 minutes` (nilai tersimpan)
5. Verifikasi Button "Save" kembali disabled

### TC-GS-GSET-51: Navigasi keluar tanpa perubahan

6. Klik menu Global Settings > Activity Log pada sidebar
7. Verifikasi berpindah langsung ke Activity Log (halaman Activity Log tampil)
8. Verifikasi Dialog Unsaved Changes tidak tampil
9. Klik menu Global Settings > General Settings pada sidebar

### TC-GS-GSET-114: Field diubah lalu dikembalikan ke nilai tersimpan

10. Pilih Session Idle Timeout `1 hour`
11. Pilih kembali Session Idle Timeout `30 minutes` (nilai tersimpan)
12. Klik menu Global Settings > Activity Log pada sidebar
13. Verifikasi berpindah langsung ke Activity Log (halaman Activity Log tampil)
14. Verifikasi Dialog Unsaved Changes tidak tampil
15. Klik menu Global Settings > General Settings pada sidebar

### TC-GS-GSET-52: Reload dengan perubahan memunculkan konfirmasi bawaan browser

16. Pilih Session Idle Timeout `1 hour`
17. Muat ulang halaman (F5)
18. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
19. Batalkan reload (tetap di halaman)
20. Verifikasi form tetap terbuka
21. Verifikasi Session Idle Timeout tetap `1 hour`

### TC-GS-GSET-53: Setelah Save sukses tidak ada dialog

22. Klik `[Save]` hingga toast sukses `Success, general settings has been saved.` tampil (Session Idle Timeout `1 hour` sudah terpilih dari langkah 16)
23. Klik menu Global Settings > Activity Log pada sidebar
24. Verifikasi berpindah langsung ke Activity Log (halaman Activity Log tampil)
25. Verifikasi Dialog Unsaved Changes tidak tampil

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Spec fungsional (state dirty form dan navigasi keluar).
- Urutan TC di spec berbeda dari urutan sumber: 29, 51, 114, 52, 53. TC-GS-GSET-51 dan TC-GS-GSET-114 didahulukan dan TC-GS-GSET-53 (satu-satunya yang menyimpan) ditaruh paling akhir (S-10, prinsip 5 aksi yang mengubah data di akhir). Setiap blok dimulai dari form bersih (nilai tersimpan `30 minutes`), kecuali TC-GS-GSET-53 yang memakai perubahan `1 hour` dari TC-GS-GSET-52 sebagai langkah 1-nya (langkah 22 menyimpan nilai itu; TC-GS-GSET-53 langkah 1 tidak diulang).
- TC-GS-GSET-52 berstatus Manual Only di TC; tetap spec dengan kebutuhan penanganan `beforeunload` ditulis di Prerequisites (konvensi bagian 2).
- Pemetaan Expected: TC-GS-GSET-29 a ke langkah 1, b ke 3, c ke 5; TC-GS-GSET-51 ke langkah 7 dan 8; TC-GS-GSET-114 ke langkah 13 dan 14; TC-GS-GSET-52 ke langkah 18, 20, dan 21; TC-GS-GSET-53 ke langkah 24 dan 25.
- Asersi absence dialog (langkah 8, 14, 25) didahului anchor positif: halaman Activity Log tampil (langkah 7, 13, 24; bagian 8b butir 2).
- Langkah penghubung: langkah 9 dan 15 (kembali ke General Settings agar blok berikutnya dimulai dari form bersih).
- Temuan untuk QA:
  - TC-GS-GSET-52: Expected menyebut "membatalkan reload"; TC tidak menyebut cara membatalkan dialog `beforeunload` (disediakan harness, Prerequisites).
  - TC-GS-GSET-53: langkah 2 menyebut "hingga toast sukses" tanpa Expected terpisah; toast sukses tidak diasersi di spec ini (Save sukses diasersi di spec 015).
