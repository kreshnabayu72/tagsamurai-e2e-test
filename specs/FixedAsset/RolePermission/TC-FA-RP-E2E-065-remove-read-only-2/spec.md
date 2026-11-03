---
id: TC-FA-RP-E2E-065-remove-read-only-2
title: "Remove Read Only (2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-218
  - TC-FA-RP-1128
  - TC-FA-RP-1132
coverage:
  web: automated
---

# Remove Read Only (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #12 (Maya Anggraeni Read Only; seluruh Global Role hanya Read), #15 (Ahmad Fauzi), #21 (Ahmad Fauzi `Manage asset & TAG` Create, Read, Update di `Head Office`), #39 (Ahmad Fauzi `Manage files` Read di `Data Center`; Detail Role `Manage Open API` terisi), #37 (Tab Read Only terisi). Pada TC-FA-RP-1132 Ahmad Fauzi di-seed berstatus Read Only dengan Group Role `Manage files` Read di `Data Center` dan `Helpdesk` (seed API) serta `Manage asset & TAG` Create, Read, Update di `Head Office`.
- Navigasi lintas modul: Settings > User > Detail User > Tab Role sub-tab Global Role atau Group Role (TC-FA-RP-1128 dan 1132).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-218: Setelah Remove Read Only, user Standard kembali eligible di popup Assign dan Detail Role tidak lagi menampilkan penugasan lama

1. Klik Tab `Read Only`
2. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`, klik `[Remove]`
3. Verifikasi muncul toast sukses: `Success, Read Only has been removed.`
4. Klik `[+ Assign]` di Tab Read Only
5. Ketik Search `Maya Anggraeni`, tekan Enter
6. Verifikasi Maya Anggraeni muncul kembali di daftar picker Assign Read Only
7. Tutup popup lewat `✕`
8. Buka Tab System lalu Detail Role `Manage Open API` dan ketik Search `Maya Anggraeni`, tekan Enter
9. Verifikasi Detail Role `Manage Open API` tidak memuat baris Maya Anggraeni (empty state hasil Search)
10. Tetapkan ulang Maya Anggraeni sebagai Read Only dengan seluruh Global Role selaras (hanya Read) lewat seeding API

### TC-FA-RP-1128: Confirm Remove Read Only mereset total Global Role: user tidak tampil di Detail Role mana pun dan kolom Users Tab System berkurang satu

11. Buka Tab System lalu catat kolom Users baris `Manage Open API` dan `Manage accounting` sebagai baseline
12. Buka Tab Read Only, klik `[⋯]` baris Maya Anggraeni lalu `Remove`, klik `[Remove]`
13. Verifikasi toast sukses `Success, Read Only has been removed.`
14. Buka Tab System dan amati kolom Users baris yang sama
15. Verifikasi kolom Users baris `Manage Open API` dan `Manage accounting` masing-masing berkurang 1 dari baseline
16. Buka Detail Role `Manage Open API` lalu ketik Search `Maya Anggraeni`, tekan Enter
17. Verifikasi baris Maya Anggraeni tidak tampil di Detail Role `Manage Open API` (empty state hasil Search)
18. Klik `(←)` pada kotak Search
19. Buka Detail Role `Manage accounting` lalu ketik Search `Maya Anggraeni`, tekan Enter
20. Verifikasi baris Maya Anggraeni tidak tampil di Detail Role `Manage accounting` (empty state hasil Search)
21. Buka Settings > User > Detail Maya Anggraeni > Tab Role sub-tab Global Role
22. Verifikasi seluruh switch Global Role OFF
23. Verifikasi seluruh checkbox Create, Read, Update, dan Delete tidak tercentang

### TC-FA-RP-1132: Confirm Remove Read Only mengosongkan seluruh penugasan Group Role di semua group: baris hilang dari Detail Role dan kolom Users berkurang

24. Tetapkan Ahmad Fauzi sebagai Read Only dengan Group Role `Manage files` Read di `Data Center` dan `Helpdesk` serta `Manage asset & TAG` Create, Read, Update di `Head Office` lewat seeding API
25. Buka Fixed Asset > Settings > Role & Permission > System lalu catat kolom Users baris Group Role `Manage files` dan `Manage asset & TAG` sebagai baseline
26. Buka Tab Read Only, klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
27. Verifikasi toast sukses `Success, Read Only has been removed.`
28. Buka Tab System dan amati kolom Users baris yang sama
29. Verifikasi kolom Users baris `Manage files` dan `Manage asset & TAG` masing-masing berkurang 1 dari baseline (dihitung per user, bukan per group)
30. Buka Detail Role Group Role `Manage files`, klik `All Groups`, lalu ketik Search `Ahmad Fauzi`, tekan Enter
31. Verifikasi baris Ahmad Fauzi tidak tampil di `Data Center` maupun `Helpdesk` (empty state hasil Search)
32. Klik `(←)` pada kotak Search
33. Buka Detail Role Group Role `Manage asset & TAG`, klik `All Groups`, lalu ketik Search `Ahmad Fauzi`, tekan Enter
34. Verifikasi baris Ahmad Fauzi tidak tampil di `Head Office` (empty state hasil Search)
35. Buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Group Role
36. Verifikasi tidak ada baris penugasan Group Role untuk Ahmad Fauzi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 36 langkah.
- Langkah penghubung (S-03): langkah 1, 7, 18, 32. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 10, 24; tidak ada `Verifikasi`.
- Asersi absence memakai empty state hasil Search sebagai anchor positif (butir 8b.2). Baseline kolom Users dicatat sebagai langkah TC dan asersi memakai selisih 1 (S-12).
- Temuan untuk QA:
  - TC-FA-RP-218 dan 1128 menggunakan Maya Anggraeni (Pre-setup #12); TC-FA-RP-1128 mensyaratkan Maya Anggraeni kembali Read Only dengan Global Role selaras sesudah TC-FA-RP-218 menghapusnya; spec memulihkannya lewat seeding API di antara blok.
  - TC-FA-RP-1132 precondition d memuat Group Role `Manage files` Read di `Helpdesk` untuk Ahmad Fauzi yang tidak ada di Pre-setup; di-seed lewat seeding API sesuai TC.
- Ukuran spec (36 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
