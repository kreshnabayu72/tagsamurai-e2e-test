---
id: TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users
title: "Screening Tab System: Navigasi ke Detail, Hover Role Name, dan Hitungan Kolom Users"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-3
  - TC-GS-ROLE-6
  - TC-GS-ROLE-7
  - TC-GS-ROLE-8
  - TC-GS-ROLE-9
  - TC-GS-ROLE-14
coverage:
  web: automated
---

# Screening Tab System: Navigasi ke Detail, Hover Role Name, dan Hitungan Kolom Users

## Prerequisites

- Mode: FE+BE.
- Aktor: Ahmad Fauzi (Total Control, Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Role & Permission > Tab System.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (lihat `suite.md`).
- Spec hanya membaca data; tidak ada data yang dibuat, diubah, atau dihapus, sehingga tidak ada pemulihan Pre-setup.
- Data Pre-setup: enam role tetap Tab System (Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role), masing-masing dengan Users ≥1. Pemegang baris "Manage TAG" yang dihitung (TC-GS-ROLE-14) mencakup Default User, user Total Control, dan user Read Only:

| Pemegang baris Manage TAG | Peran dalam hitungan |
|---|---|
| `Budi Santoso` | Default User (Pre-setup #2) |
| `Siti Nurhaliza` | Read Only, punya baris role Manage TAG (Pre-setup #4) |
| `{user Total Control pemegang baris Manage TAG}` | Total Control; disediakan tim FE (TC tidak menyebut nama user Total Control yang punya baris Manage TAG) |

- Total baris Detail "Manage TAG" dicatat dari info pagination di Detail pada saat spec berjalan (langkah 38); angka itu dibandingkan dengan kolom Users Tab System.
- Kemampuan teknis: pembacaan warna teks dan dekorasi teks (underline) saat hover, serta pembacaan atribut icon dan severity pada row action.

## Test Steps

### TC-GS-ROLE-3: Screening halaman Role & Permission Tab System

1. Verifikasi breadcrumb "Role & Permission > System" tampil
2. Verifikasi segmen "System" pada breadcrumb bukan link
3. Verifikasi Tab `Total Control`, `Read Only`, dan `System` tampil dengan Tab `System` aktif
4. Verifikasi Table Tools memuat `Search`, `Download`, dan `Changelog`
5. Verifikasi Table Tools tidak memuat `Filter` dan `[+ Assign]`
6. Verifikasi kolom tabel berurutan `Role Name | Users | Actions (⋯)`
7. Verifikasi kolom Role Name, Users, dan Actions (⋯) unsortable
8. Klik header kolom Actions (⋯)
9. Verifikasi overlay Column Visibility terbuka
10. Tutup overlay Column Visibility dengan Esc
11. Verifikasi urutan baris tetap: Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role
12. Verifikasi Role Name tampil sebagai text link
13. Verifikasi kolom Users berisi angka bulat tanpa pemisah ribuan
14. Verifikasi kolom Users setiap baris bernilai ≥1
15. Verifikasi Pagination tidak tampil

### TC-GS-ROLE-9: Hover Role Name di Tab System

16. Arahkan kursor ke Role Name `Import data`
17. Verifikasi warna teks berubah ke warna primary Global Settings
18. Verifikasi Role Name `Import data` tanpa underline
19. Pindahkan kursor keluar dari Role Name `Import data`
20. Verifikasi warna teks kembali ke warna body text

### TC-GS-ROLE-6: Buka Detail lewat klik Role Name di Tab System

21. Klik text link Role Name `Manage TAG`
22. Verifikasi halaman Detail "Manage TAG" terbuka sebagai full page (bukan modal)
23. Verifikasi breadcrumb "Role & Permission > System > Detail" tampil
24. Klik segmen "System" pada breadcrumb

### TC-GS-ROLE-7: Buka Detail lewat row action Detail di Tab System

25. Klik `⋯` pada baris `Manage TAG`
26. Verifikasi overlay row action hanya berisi `Detail`
27. Verifikasi `Detail` memakai icon FileInfoLine
28. Verifikasi `Detail` berseverity dark
29. Klik `Detail`
30. Verifikasi halaman Detail "Manage TAG" terbuka sebagai full page
31. Verifikasi breadcrumb "Role & Permission > System > Detail" tampil
32. Klik segmen "System" pada breadcrumb

### TC-GS-ROLE-8: Kembali dari Detail ke Tab System lewat breadcrumb

33. Klik Role Name `Manage files`
34. Klik segmen "System" pada breadcrumb
35. Verifikasi kembali ke Tab System dengan Tab `System` aktif
36. Verifikasi breadcrumb "Role & Permission > System" tampil

### TC-GS-ROLE-14: Kolom Users Tab System menghitung semua pemegang baris termasuk TC/RO

37. Klik Role Name `Manage TAG`
38. Catat total baris pada info pagination Detail "Manage TAG"
39. Untuk setiap baris tabel "Pemegang baris Manage TAG" (langkah 39 sampai 41): ketik Search `{nama pemegang}`, tekan Enter
40. Untuk setiap baris tabel "Pemegang baris Manage TAG" (langkah 39 sampai 41): Verifikasi baris `{nama pemegang}` tampil di Detail "Manage TAG"
41. Untuk setiap baris tabel "Pemegang baris Manage TAG" (langkah 39 sampai 41): klik `(←)` pada kotak Search
42. Klik segmen "System" pada breadcrumb
43. Verifikasi angka kolom Users baris `Manage TAG` sama dengan total baris Detail "Manage TAG" yang dicatat pada langkah 38
44. Verifikasi tidak ada baris role dengan Users 0

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-GS-ROLE-3 (screening) dan TC-GS-ROLE-9 (hover) dijalankan di Tab System lebih dulu; TC-GS-ROLE-6, 7, 8, dan 14 menyusul karena berpindah ke Detail. Perubahan urutan dari nomor TC mengikuti prinsip screening di awal.
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): klik header Actions (langkah 8, menjalankan klausa "header = overlay Column Visibility" Expected TC-GS-ROLE-3) dan menutup overlay dengan Esc (langkah 10); kembali ke Tab System lewat breadcrumb (langkah 24 dan 32); mengosongkan kotak Search (langkah 41).
- Langkah 39 sampai 41 diulang untuk tiga baris tabel Prerequisites ("Pemegang baris Manage TAG"); ekspansi menambah enam langkah (jumlah ekspansi 50 langkah). Pengulangan memverifikasi klausa Expected b TC-GS-ROLE-14 ("hitungan memuat Default User, user Total Control, dan user Read Only") karena Detail tidak menampilkan kolom tier.
- Expected TC-GS-ROLE-7 b ("sama dengan jalur klik Role Name") diasersi sebagai full page dan breadcrumb yang sama dengan TC-GS-ROLE-6 (langkah 30 dan 31).
- Spec melewati sekitar 35 langkah (44 langkah nominal, 50 dengan ekspansi). Alasan: seluruh blok berkelas sama (screening/navigasi tanpa aksi tulis, satu akun, satu dataset Pre-setup) dan jumlahnya berasal dari aturan S-01 (satu `Verifikasi` per klausa Expected) serta pengulangan tiga pemegang baris pada TC-GS-ROLE-14. Tiap blok TC berawal dari Tab System atau dari Detail yang dibuka sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-GS-ROLE-14 precondition c menyebut Detail "Manage TAG" memuat user Total Control dan Read Only tetapi tidak menyebut nama user Total Control pemegang baris Manage TAG; spec memakai "disediakan tim FE" (S-11).
  - TC-GS-ROLE-9 Expected a menyebut warna "primary Global Settings (hitam/kontras)" tanpa nilai warna; spec mengasersi perubahan ke warna primary tanpa nilai.
  - TC-GS-ROLE-3 tidak menyebut cara mengamati Pagination yang tidak tampil; spec mengasersi tidak ada Pagination.
