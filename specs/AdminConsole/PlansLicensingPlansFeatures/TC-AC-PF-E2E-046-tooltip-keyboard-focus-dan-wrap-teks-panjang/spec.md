---
id: TC-AC-PF-E2E-046-tooltip-keyboard-focus-dan-wrap-teks-panjang
title: Tooltip Dapat Diakses Lewat Keyboard Focus dan Teks Panjang Wrap pada Lebar Maksimum 400px
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-644
coverage:
  web: automated
---

# Tooltip Dapat Diakses Lewat Keyboard Focus dan Teks Panjang Wrap pada Lebar Maksimum 400px

## Prerequisites

- Mode: FE+BE
- Akun aktor: #8 `groupMixPrincipal_automated_{namaCompany}@qwertysystem.net` (Manage plans & licensing: Read dan Update; Group Role Manage active client dengan Zero Access pada group PT Timur Jaya; password dari env `AC_PF_GM_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan D (`Growth` v5 dengan client `PT Timur Jaya` Zero Access), Dataset Plan P (custom plan `Paket Turun` v3 dengan client `PT Turun Satu` Active v1 dan `PT Turun Dua` Active v2; delta downgrade pada `PT Turun Satu`), dan Dataset Plan A (custom `Growth Tier` aktif). Spec hanya membaca data ini; Edit `Growth Tier` ditutup tanpa menyimpan. Nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis: kemampuan memindahkan fokus dengan tombol Tab dan membaca tooltip yang tampil saat fokus; fixture backend (pemulihan Dataset Pre-setup) disediakan tim FE/BE dan dinyatakan di `suite.md`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PF-644: tooltip lewat keyboard focus

1. Buka Plan Detail `Growth` (klik Plan Name).
2. Klik Tab Assigned Clients.
3. Buka Overlay Row Action pada `PT Timur Jaya`.
4. Pindahkan fokus dengan tombol Tab ke opsi `Detail` yang Disabled.
5. Verifikasi opsi `Detail` Disabled menampilkan tooltip "You do not have permission to view or manage clients in this group." saat menerima fokus.
6. Kembali ke list lewat Breadcrumb.
7. Klik tab Custom.
8. Buka Plan Detail `Paket Turun`.
9. Klik Tab Assigned Clients.
10. Pindahkan fokus dengan tombol Tab ke icon peringatan `PT Turun Satu`.
11. Verifikasi icon peringatan menampilkan tooltip "This client cannot receive a push update — the current plan version reduces one or more features. Manage via Allocation > Client Subscription." saat menerima fokus.
12. Verifikasi teks tooltip wrap ke baris berikutnya tanpa terpotong (tanpa ellipsis).
13. Verifikasi lebar tooltip tidak melebihi 400px.
14. Kembali ke list lewat Breadcrumb.
15. Buka Overlay Row Action pada `Growth Tier`.
16. Klik `Edit`.
17. Matikan Open API.
18. Pindahkan fokus dengan tombol Tab ke field API call quota yang Disabled.
19. Verifikasi field API call quota Disabled menampilkan tooltip `Turn on Open API to set an API call quota.` saat menerima fokus.
20. Klik segmen Breadcrumb `Plans & Features`.
21. Verifikasi dialog `Unsaved Changes` tampil.
22. Klik `[Leave]`.

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 8, 9 (membuka Plan Detail dan Tab Assigned Clients), langkah 6 dan 14 (kembali ke list), langkah 7 (pindah tab), langkah 20 sampai 22 (menutup form dirty, S-08; `Verifikasi` dialog `Unsaved Changes` pada langkah 21 diwajibkan S-08).
- Pembagian TC lintas spec: TC-AC-PF-696 sampai TC-AC-PF-699 ada di spec 043.
- Temuan untuk QA:
  - TC-AC-PF-644 langkah 3 mematikan Open API pada `Growth Tier`; TC tidak menyebut apakah Open API pada `Growth Tier` sudah ON di Pre-setup (Dataset Plan A tidak merinci). Spec mengikuti langkah TC.
  - TC-AC-PF-644 Expected a menyebut tooltip pada opsi Disabled "saat menerima fokus" tanpa menyebut apakah overlay row action harus dibuka lewat keyboard; spec membuka overlay dengan klik (langkah 3) lalu memindahkan fokus dengan Tab.
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
