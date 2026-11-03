---
id: TC-FA-LBL-E2E-033-menutup-form-create-form-dikembalikan-backdrop-reload-dan-pindah-route
title: "Menutup Form Create: Form Dikembalikan, Backdrop, Reload, dan Pindah Route (bagian 2/2)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-96
  - TC-FA-LBL-97
  - TC-FA-LBL-98
  - TC-FA-LBL-99
coverage:
  web: automated
---

# Menutup Form Create: Form Dikembalikan, Backdrop, Reload, dan Pindah Route (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Kemampuan teknis: menangani konfirmasi bawaan browser (`beforeunload`) pada reload (menerima atau membatalkan) untuk TC-FA-LBL-98 (S-08).
- Spec ini tidak membuat atau menyimpan label; tidak ada cleanup data.

## Test Steps

### TC-FA-LBL-96: Form yang diketik lalu dikembalikan identik dengan kondisi awal dianggap bersih

1. Klik `[+ Label]`
2. Ketik `Revert 96` di Label Name
3. Hapus seluruh teks sampai kosong
4. Klik icon `[✕]`
5. Verifikasi modal langsung tertutup
6. Verifikasi tidak ada dialog `You have unsaved changes. Are you sure you want to leave?`

### TC-FA-LBL-97: Klik backdrop modal Create Label tidak menutup modal

7. Klik `[+ Label]`
8. Klik area gelap di luar modal
9. Verifikasi modal tetap terbuka
10. Ketik `Backdrop 97` di Label Name
11. Klik area gelap di luar modal lagi
12. Verifikasi modal tetap terbuka
13. Verifikasi input Label Name dipertahankan
14. Verifikasi dialog Unsaved Changes tidak tampil

### TC-FA-LBL-98: Form Create terisi memicu konfirmasi bawaan browser saat reload

15. Ganti isi Label Name dengan `Reload 98`
16. Tekan F5
17. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
18. Batalkan konfirmasi browser
19. Kosongkan Label Name
20. Tekan F5
21. Verifikasi halaman dimuat ulang tanpa konfirmasi karena form bersih

### TC-FA-LBL-99: Berpindah route internal saat form Create terisi memunculkan dialog Unsaved Changes

22. Klik `[+ Label]`
23. Ketik `Route 99` di Label Name
24. Klik item menu lain pada sidebar
25. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
26. Verifikasi navigasi dicegat
27. Klik `[Cancel]`
28. Verifikasi tetap di form dengan input dipertahankan
29. Klik item menu lain pada sidebar
30. Klik `[Leave]`
31. Verifikasi navigasi berlanjut
32. Verifikasi form tertutup

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Modal yang dibuka pada TC-FA-LBL-97 dipakai TC-FA-LBL-98 (langkah 15 mengganti isi Label Name `Backdrop 97` menjadi `Reload 98`), karena langkah 1 TC-FA-LBL-98 hanya membuka modal yang sama (prinsip 6).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 15.
- Reload hanya ditulis karena kemampuan menangani dialog `beforeunload` tercantum di `## Prerequisites` (S-08). Spec berakhir di luar halaman Labels setelah TC-FA-LBL-99; hook `beforeEach` suite membuka tab Labels untuk spec berikutnya.
- Temuan untuk QA:
  - TC-FA-LBL-99 tidak menyebut item sidebar yang diklik; spec memakai "item menu lain pada sidebar" seperti TC.
  - TC-FA-LBL-97 dan TC-FA-LBL-99 memakai Label Name yang tidak disimpan, sehingga tidak memakai suffix.
