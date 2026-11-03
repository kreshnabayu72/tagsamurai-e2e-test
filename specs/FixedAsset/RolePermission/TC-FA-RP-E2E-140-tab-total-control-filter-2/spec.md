---
id: TC-FA-RP-E2E-140-tab-total-control-filter-2
title: "Tab Total Control: Filter (2/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-483
  - TC-FA-RP-484
  - TC-FA-RP-485
  - TC-FA-RP-486
coverage:
  web: automated
---

# Tab Total Control: Filter (2/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Position, Division, Status, Activation Status, Temporary User, dan Modified By memiliki dua nilai distinct atau lebih) dan #37 (Tab Read Only empat baris). Endah Susanti (Procurement Officer, Pre-setup #15) bukan Total Control dan menjadi pembanding absence opsi `Procurement Officer`. Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.

## Test Steps

### Isi opsi dropdown Filter (TC 483)

1. Klik ikon Filter.
2. Buka dropdown field Position.
3. Verifikasi opsi Position: `Asset Custodian`, `Facility Officer`, `Finance Officer`, `Finance Supervisor`, `HR Manager`, `Operations Manager, Region 1`, `System Administrator`, `Warehouse Staff`.
4. Verifikasi opsi `Procurement Officer` tidak muncul pada dropdown Position.
5. Tutup dropdown dengan Esc.
6. Buka dropdown field Division.
7. Verifikasi opsi Division: `Accounting & Tax`, `Asset Management "North"`, `Finance`, `General Affairs`, `HR`, `IT Operations`, `Logistics`.
8. Tutup dropdown dengan Esc.
9. Buka dropdown field Status.
10. Verifikasi opsi Status: `Active`, `Inactive`.
11. Tutup dropdown dengan Esc.
12. Buka dropdown field Activation Status.
13. Verifikasi opsi Activation Status: `Activated`, `Pending Activation`, `Pending Email Confirmation`.
14. Tutup dropdown dengan Esc.
15. Buka dropdown field Temporary User.
16. Verifikasi opsi Temporary User: `Yes`, `No`.
17. Tutup dropdown dengan Esc.
18. Buka dropdown field Modified By.
19. Verifikasi opsi Modified By: `Admin Utama`, `Prasetyo Hadi`, `Siti Rahmawati`, `System`.
20. Tutup dropdown dengan Esc.

### Search internal dropdown (TC 484)

21. Buka dropdown field Position.
22. Ketik `fin` pada kotak pencarian dropdown.
23. Verifikasi daftar opsi Position menyempit ke opsi yang memuat `fin` tanpa membedakan huruf besar kecil: `Finance Officer` dan `Finance Supervisor`.
24. Ganti isi kotak pencarian dropdown dengan `zzz`.
25. Verifikasi keadaan tanpa opsi cocok tampil.
26. Tutup dropdown dengan Esc.

### Logika OR dalam satu field (TC 485)

27. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
28. Pilih dua opsi pada field Position: `Finance Officer` dan `HR Manager`.
29. Klik `[Apply]`.
30. Verifikasi baris Siti Rahmawati, Fitri Handayani, dan Siti Rahayu tampil (gabungan OR, bukan irisan).
31. Verifikasi baris lain tidak tampil.
32. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Logika AND antar field (TC 486)

33. Pilih `Finance Officer` pada field Position.
34. Pilih `Logistics` pada field Division.
35. Klik `[Apply]`.
36. Verifikasi tabel menampilkan irisan baris yang memenuhi kedua kriteria: tidak ada baris tampil (empty state `No results found`).
37. Klik `[Clear Field]`, lalu klik `[Apply]`.

## Notes

- Alasan di atas 35 langkah: seluruh blok berkelas fungsional sama (Filter Panel tabel yang sama, dataset Pre-setup #36 yang sama) dan berdiri sendiri karena dropdown ditutup dan filter dibersihkan di akhir tiap blok; tambahan langkah hanya penutupan dropdown dan pembersihan filter, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1, 2, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 22, 24, 26, 28, 29, 32, 33, 34, 35, dan 37. Langkah penutup dropdown dengan Esc (5, 8, 11, 14, 17, 20, 26) menjaga satu dropdown terbuka pada satu waktu (S-09). Langkah 32 dan 37 mengembalikan filter ke keadaan kosong.
- Langkah 4 adalah asersi absence opsi; pembanding positifnya opsi Position yang tampil pada langkah 3. Langkah 31 adalah asersi absence baris; pembanding positifnya langkah 27 dan 30.
- Temuan untuk QA:
  - TC 486 menyebut "irisan baris yang memenuhi kedua kriteria" tanpa menyebut nama baris. Pada Pre-setup #36 Position `Finance Officer` (Siti Rahmawati dan Fitri Handayani) dan Division `Logistics` (Ahmad Fauzi dan Budi Santoso) tidak beririsan, sehingga irisan kosong; spec mengasersi empty state `No results found` (langkah 36), dan perlu konfirmasi QA apakah Data Uji dimaksudkan menghasilkan baris.
  - TC 484 tidak menyebut teks keadaan tanpa opsi cocok pada dropdown; spec mengasersi keadaan itu tanpa teks literal.
