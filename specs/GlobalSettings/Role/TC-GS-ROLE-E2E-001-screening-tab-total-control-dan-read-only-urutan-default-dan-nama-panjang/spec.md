---
id: TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-read-only-urutan-default-dan-nama-panjang
title: "Screening Tab Total Control dan Tab Read Only: Urutan Default, Baris Default User, Status Inactive, dan Nama Panjang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-1
  - TC-GS-ROLE-2
  - TC-GS-ROLE-10
  - TC-GS-ROLE-11
  - TC-GS-ROLE-24
coverage:
  web: automated
---

# Screening Tab Total Control dan Tab Read Only: Urutan Default, Baris Default User, Status Inactive, dan Nama Panjang

## Prerequisites

- Mode: FE+BE.
- Aktor: Ahmad Fauzi (Total Control, Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Role & Permission dengan Tab Total Control aktif. Spec tidak menguji navigasi sidebar.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (lihat `suite.md`).
- Spec hanya membaca data; tidak ada data yang dibuat, diubah, atau dihapus, sehingga tidak ada pemulihan Pre-setup.
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup `tc-role.md`):
  - Tab Total Control: Ahmad Fauzi, Budi Santoso (Default User, Pre-setup #2), Dewi Lestari (Total Control, status user Inactive, Pre-setup #3), Raden Mas Bagus Prasetyo Wicaksono Adiningrat Hadiprojo (Total Control, nama 60 karakter, tanpa foto, Pre-setup #15), serta volume ≥11 user (Pre-setup #17) dan Bayu Nugraha (Pre-setup #19) sehingga Pagination aktif.
  - Tab Read Only: Siti Nurhaliza (Finance Staff, Finance, Active) dan Rina Putri (HR Manager, HR, Inactive) (Pre-setup #4); keduanya tampil di halaman 1 Tab Read Only. Pre-setup #19 menambah Intan Permata (Read Only).
  - State Pre-setup yang diharapkan: Dewi Lestari, Siti Nurhaliza, dan Rina Putri berada pada kondisi Pre-setup (catatan "Reset Pre-setup per TC" di `tc-role.md`); spec lain yang mengubah user tersebut memulihkannya.
- Kemampuan teknis: pembacaan ukuran lebar kolom dan teks sel (untuk asersi nama tidak terpotong) serta pembacaan atribut visual (avatar placeholder, tipe tombol primary).

## Test Steps

### TC-GS-ROLE-1: Screening halaman Role & Permission Tab Total Control

1. Verifikasi breadcrumb "Role & Permission > Total Control" tampil
2. Verifikasi segmen "Total Control" pada breadcrumb bukan link
3. Verifikasi breadcrumb berada di luar SectionCard
4. Verifikasi Tab `Total Control`, `Read Only`, dan `System` tampil
5. Verifikasi Tab `Total Control` aktif
6. Verifikasi Table Tools rata kanan memuat `Search | Filter | Download | Changelog | [+ Assign]`
7. Verifikasi `[+ Assign]` bertipe primary
8. Verifikasi section description "Total Control applies to Global Settings only — it does not grant access to other TAG Samurai products."
9. Verifikasi kolom tabel berurutan `Name | Position | Division | Status | Modified By | Last Updated | Actions (⋯)`
10. Verifikasi kolom Name, Position, Division, Status, Modified By, dan Last Updated sortable
11. Verifikasi kolom Actions (⋯) unsortable
12. Klik header kolom Actions (⋯)
13. Verifikasi overlay Column Visibility terbuka
14. Verifikasi CTA `[Setup Column]` tampil di dalam overlay Column Visibility
15. Tutup overlay Column Visibility dengan Esc
16. Verifikasi kolom Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field aktif tidak tampil
17. Verifikasi tidak ada kolom checkbox seleksi baris dan tidak ada kolom CRUD
18. Verifikasi Pagination default 10 baris/halaman

### TC-GS-ROLE-10: Default sort Tab Total Control dan posisi baris Default User

19. Verifikasi baris tabel halaman 1 terurut Name A-Z tanpa menyentuh sort
20. Verifikasi baris `Ahmad Fauzi` berada sebelum baris `Budi Santoso`
21. Verifikasi kolom Position baris `Budi Santoso` bernilai "—"
22. Verifikasi kolom Division baris `Budi Santoso` bernilai "—"
23. Verifikasi kolom Status baris `Budi Santoso` bernilai "Active"
24. Verifikasi kolom Modified By baris `Budi Santoso` bernilai "—"
25. Verifikasi kolom Last Updated baris `Budi Santoso` bernilai "—"

### TC-GS-ROLE-11: User Inactive tetap tampil di Tab Total Control

26. Ketik Search `Dewi Lestari`, tekan Enter
27. Verifikasi baris `Dewi Lestari` tampil
28. Verifikasi badge Status "Inactive" tampil pada baris `Dewi Lestari`
29. Klik `⋯` pada baris `Dewi Lestari`
30. Verifikasi row action `Remove` tampil dan enabled
31. Tutup row action menu dengan Esc
32. Klik `(←)` pada kotak Search

### TC-GS-ROLE-24: Name panjang tidak terpotong dan avatar placeholder

33. Ketik Search `Raden Mas Bagus Prasetyo Wicaksono Adiningrat Hadiprojo`, tekan Enter
34. Verifikasi sel Name menampilkan `Raden Mas Bagus Prasetyo Wicaksono Adiningrat Hadiprojo` utuh tanpa ".."
35. Verifikasi kolom Name melebar mengikuti konten
36. Verifikasi avatar circle placeholder generik tampil di kiri nama
37. Klik `(←)` pada kotak Search

### TC-GS-ROLE-2: Screening halaman Role & Permission Tab Read Only

38. Klik Tab Read Only
39. Verifikasi breadcrumb "Role & Permission > Read Only" tampil
40. Verifikasi segmen "Read Only" pada breadcrumb bukan link
41. Verifikasi Tab `Total Control`, `Read Only`, dan `System` tampil
42. Verifikasi Tab `Read Only` aktif
43. Verifikasi Table Tools memuat `Search | Filter | Download | Changelog | [+ Assign]`
44. Verifikasi section description "Read Only applies to Global Settings only — it does not grant access to other TAG Samurai products."
45. Verifikasi kolom tabel berurutan `Name | Position | Division | Status | Modified By | Last Updated | Actions (⋯)`
46. Verifikasi kolom Name, Position, Division, Status, Modified By, dan Last Updated sortable
47. Verifikasi kolom Actions (⋯) unsortable
48. Klik header kolom Actions (⋯)
49. Verifikasi overlay Column Visibility terbuka
50. Verifikasi CTA `[Setup Column]` tampil di dalam overlay Column Visibility
51. Tutup overlay Column Visibility dengan Esc
52. Verifikasi baris `Siti Nurhaliza` tampil dengan Status "Active"
53. Verifikasi baris `Rina Putri` tampil dengan Status "Inactive"
54. Verifikasi tidak ada baris `Budi Santoso` (Default User)
55. Verifikasi tidak ada kolom checkbox seleksi dan tidak ada kolom CRUD
56. Verifikasi Pagination default 10 baris/halaman
57. Klik `⋯` pada baris `Siti Nurhaliza`
58. Verifikasi row action `Remove` tampil
59. Tutup row action menu dengan Esc

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: TC-GS-ROLE-1, 10, 11, 24 (semuanya Tab Total Control, layar awal dari hook `beforeEach`), lalu pindah ke Tab Read Only untuk TC-GS-ROLE-2. TC-GS-ROLE-2 dijalankan terakhir agar tidak ada pembukaan ulang layar; TC-GS-ROLE-10, 11, dan 24 memakai tab yang sudah termuat.
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): menutup overlay atau row action menu dengan Esc (langkah 15, 31, 51, 59), mengosongkan kotak Search (langkah 32 dan 37), dan pindah ke Tab Read Only (langkah 38). Klik header Actions (langkah 12 dan 48) menjalankan klausa "header klik = buka overlay Column Visibility" pada Expected TC-GS-ROLE-1 dan TC-GS-ROLE-2.
- Klausa "body per baris = row action Remove" pada kolom Actions TC-GS-ROLE-1 dan TC-GS-ROLE-2 diasersi pada baris `Dewi Lestari` (langkah 29 dan 30, bersama Expected TC-GS-ROLE-11) dan baris `Siti Nurhaliza` (langkah 57 dan 58).
- Dewi Lestari dan baris Raden Mas… dicari lewat Search karena Pre-setup #17 dan #19 membuat halaman 1 berisi lebih dari tiga nama sehingga posisi baris tidak dapat dipastikan.
- Spec melewati sekitar 35 langkah (59 langkah). Alasan: seluruh blok berkelas sama (screening tanpa aksi tulis, satu akun, satu dataset Pre-setup) dan jumlah langkah berasal dari aturan S-01 (satu `Verifikasi` per klausa Expected TC-GS-ROLE-1 dan TC-GS-ROLE-2, masing-masing sekitar 20 langkah) bukan dari aksi berlapis. Blok Tab Read Only (langkah 38 sampai 59) dimulai dari pindah tab sehingga tetap bermakna walau blok Tab Total Control gagal, dan sebaliknya.
- Temuan untuk QA:
  - TC-GS-ROLE-10 Expected a menyebut urutan "Ahmad Fauzi, Budi Santoso, Dewi Lestari", padahal Pre-setup #17 (≥11 user) dan #19 (Bayu Nugraha, Intan Permata) menambah nama di antaranya; spec mengasersi urutan A-Z halaman 1 dan Ahmad Fauzi sebelum Budi Santoso, dan tidak mengasersi posisi Dewi Lestari terhadap kedua nama itu.
  - TC-GS-ROLE-1 Expected "kolom Actions ... header klik = buka overlay Column Visibility → CTA [Setup Column]" dan "segmen ... di luar SectionCard" tidak menyebut cara pengamatan; spec memakai klik header dan pengamatan posisi breadcrumb.
  - TC-GS-ROLE-24 tidak menyebut halaman tempat baris Pre-setup #15 berada; spec memakai Search nama lengkap.
