---
id: TC-FA-FAAM-E2E-077-edit-dialog-change-default-addon-tampil-b
title: "Edit Ber-Aset: Dialog Change Default Addon (Pengurangan Tunggal, Pending Quota, Unenrolled)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-680
  - TC-FA-FAAM-720
  - TC-FA-FAAM-721
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog Change Default Addon (Pengurangan Tunggal, Pending Quota, Unenrolled)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #14q: `Solo Trans Item` (Total Asset 1: Default Addon `Tracking`, aset Active `enrolled_via_default` dengan transaksi aktif di Tracking); #30 `Solo Pending Item` (Total Asset 2: satu aset Active ter-pairing TAG `QR` dan satu aset Active belum TAG pairing, tanpa Default Addon; lisensi Tracking tersedia 0); #30b `Solo Unenroll Item` (Total Asset 1: Default Addon `Audit`, aset Active `enrolled_via_default` tanpa transaksi aktif). Ketiganya hanya dibuka dan dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-680: Dialog Change Default Addon pengurangan memakai bentuk tunggal In Transaction dan menghilangkan klausa Unenrolled bernilai 0

1. Ketik Search `Solo Trans Item`, tekan Enter
2. Klik `⋯` baris `Solo Trans Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Lepas Default Addon `Tracking`
4. Klik `[Save]`
5. Verifikasi dialog `Change Default Addon` dengan tombol `[Cancel]` dan `[Save]` memuat `Removing Tracking:` dengan klausa `1 asset has an active transaction — it will stay enrolled and be unenrolled once that transaction completes.` lalu `Are you sure you want to save this change?`
6. Verifikasi tidak ada klausa `will be unenrolled.`
7. Klik `[Cancel]` pada dialog
8. Tambahkan kembali Default Addon `Tracking` (kembali ke nilai tersimpan)
9. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

### TC-FA-FAAM-720: Dialog Change Default Addon penambahan memakai bentuk tunggal pending quota dan menunggu TAG pairing serta menghilangkan klausa Enrolled bernilai 0

10. Ganti isi kotak search dengan `Solo Pending Item`, tekan Enter
11. Klik `⋯` baris `Solo Pending Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
12. Tambahkan Default Addon `Tracking`
13. Klik `[Save]`
14. Verifikasi dialog `Change Default Addon` dengan tombol `[Cancel]` dan `[Save]` memuat `Adding Tracking:` dengan klausa `1 asset will be set to pending quota.` dan klausa `1 asset is waiting for TAG pairing.`
15. Verifikasi tidak ada klausa `will be enrolled`
16. Verifikasi kalimat penutup `Are you sure you want to save this change?` tampil
17. Klik `[Cancel]` pada dialog
18. Lepas chip Default Addon `Tracking` (kembali ke nilai tersimpan)
19. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

### TC-FA-FAAM-721: Dialog Change Default Addon pengurangan memakai bentuk tunggal Unenrolled dan menghilangkan klausa In Transaction bernilai 0

20. Ganti isi kotak search dengan `Solo Unenroll Item`, tekan Enter
21. Klik `⋯` baris `Solo Unenroll Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
22. Lepas Default Addon `Audit`
23. Klik `[Save]`
24. Verifikasi dialog `Change Default Addon` dengan tombol `[Cancel]` dan `[Save]` memuat `Removing Audit:` dengan klausa `1 asset will be unenrolled.`
25. Verifikasi tidak ada klausa yang memuat `active transaction`
26. Verifikasi kalimat penutup `Are you sure you want to save this change?` tampil
27. Klik `[Cancel]` pada dialog
28. Tambahkan kembali Default Addon `Audit` (kembali ke nilai tersimpan)
29. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 10, dan 20 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 7, 17, dan 27; pengembalian addon ke nilai tersimpan pada langkah 8, 18, dan 28 lalu penutupan modal bersih pada langkah 9, 19, dan 29 (tanpa dialog karena form sama dengan nilai tersimpan).
- Seluruh dialog dibatalkan sehingga fixture tidak berubah. Verifikasi isi dialog menjadi anchor bagi asersi ketiadaan klausa (bagian 8b butir 2).
