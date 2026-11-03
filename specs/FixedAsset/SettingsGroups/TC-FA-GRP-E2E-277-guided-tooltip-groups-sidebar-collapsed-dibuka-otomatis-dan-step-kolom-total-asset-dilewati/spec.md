---
id: TC-FA-GRP-E2E-277-guided-tooltip-groups-sidebar-collapsed-dibuka-otomatis-dan-step-kolom-total-asset-dilewati
title: "Guided Tooltip Groups: Sidebar Collapsed Dibuka Otomatis dan Step Kolom Total Asset Dilewati saat Kolom Disembunyikan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-41
  - TC-FA-GRP-970
coverage:
  web: automated
---

# Guided Tooltip Groups: Sidebar Collapsed Dibuka Otomatis dan Step Kolom Total Asset Dilewati saat Kolom Disembunyikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Spec ini mengatur flag Guided Tooltip `fa-settings-groups` sendiri sesudah hook suite menyetelnya `seen`: kemampuan menyetel flag menjadi belum diset atau `seen` untuk akun aktor disediakan tim FE/BE; flag dipulihkan ke `seen` di hook `after`.
- State yang diubah spec ini dan dipulihkan: (a) preferensi sidebar (Open/Collapse) akun aktor, dikembalikan Open oleh langkah 13 dan dihapus di hook `after`; (b) konfigurasi kolom Setup Column Groups List (kolom Total Asset di-hide pada langkah 14 sampai 16), dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat [Reset to Default]).
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9).
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini mengubah preferensi sidebar dan konfigurasi kolom akun aktor serta flag Guided Tooltip, semuanya dipulihkan di hook `after`.

## Test Steps

### TC-FA-GRP-970: Sidebar collapsed dibuka otomatis selama Step 1

1. Klik toggle sidebar untuk menutup sidebar
2. Verifikasi sidebar tertutup (preferensi collapsed tersimpan)
3. Setel flag `fa-settings-groups` menjadi belum diset
4. Muat ulang halaman dengan F5
5. Verifikasi sidebar dibuka otomatis selama Step 1 (Sidebar Group Tree)
6. Verifikasi Step 1 tidak dilewati dan penomor tetap `Step 1 of 3`
7. Klik [Next]
8. Klik [Next]
9. Klik [Done]
10. Verifikasi sidebar kembali collapsed
11. Muat ulang halaman dengan F5
12. Verifikasi sidebar tetap collapsed (state persisten tidak berubah)
13. Klik toggle sidebar untuk membuka sidebar

### TC-FA-GRP-41: Step kolom Total Asset dilewati saat kolom di-hide

14. Klik header kolom Column Visibility (⋯)
15. Hapus centang kolom Total Asset pada Setup Column
16. Klik [Save]
17. Verifikasi kolom Total Asset tidak tampil pada tabel
18. Setel flag `fa-settings-groups` menjadi belum diset
19. Muat ulang halaman dengan F5
20. Verifikasi walkthrough muncul otomatis pada Step 1
21. Klik [Next]
22. Verifikasi Step 2 menyorot kolom Function dengan judul `Assignable & Disposal Groups`
23. Verifikasi penomor `Step 2 of 2`
24. Verifikasi [Next] berubah menjadi [Done]
25. Klik [Done]
26. Verifikasi step `Asset Count` tidak ditampilkan (dilewati)

## Notes

- Langkah penghubung (S-03): langkah 1 (menyiapkan sidebar collapsed), langkah 3 dan 18 (menyetel flag), langkah 4 dan 19 (muat ulang agar flag dievaluasi, menggantikan "Buka Fixed Asset > Settings > Groups" karena halaman sudah dibuka hook `beforeEach`), langkah 13 (memulihkan sidebar Open), langkah 14 sampai 16 (menyembunyikan kolom Total Asset sebagai precondition TC-FA-GRP-41).
- Urutan TC dalam spec: 970, 41. TC-FA-GRP-41 terakhir karena mengubah konfigurasi kolom yang dipulihkan di hook `after`.
- Pembagian TC lintas spec: TC-FA-GRP-38, 39, dan 1094 (Guided Tooltip navigasi keluar, keyboard, resize) ada di spec 013.
- Temuan untuk QA:
  - TC-FA-GRP-970 butir b menyebut "[Done] (atau [Skip])"; spec memakai jalur [Done] sesuai langkah TC.
  - TC-FA-GRP-41 mengharapkan penomor `Step [Current Step] of 2` tanpa menyebut apa yang tampil sesudah Step Function; spec mengasersi [Next] menjadi [Done] mengikuti pola Step terakhir TC-FA-GRP-34.
