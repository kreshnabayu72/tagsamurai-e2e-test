---
id: TC-AC-ACC-E2E-146-dua-sesi-konflik-change-partner-dan-delete
title: "Dua Sesi Admin: Konflik 409 pada Change Partner dan Delete Client yang Sudah Dihapus Sesi Lain Sukses Tanpa Baris Changelog Baru"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-187
  - TC-AC-ACC-961
coverage:
  web: automated
---

# Dua Sesi Admin: Konflik 409 pada Change Partner dan Delete Client yang Sudah Dihapus Sesi Lain Sukses Tanpa Baris Changelog Baru

## Prerequisites

- Mode: FE+BE.
- Konteks (kelas c, dua sesi UI yang kedua-duanya diasersi): Sesi A dan Sesi B berjalan bersamaan pada kedua TC.
- Akun aktor (urutan blok = urutan akun; Step ganti akun eksplisit di kedua sesi):

| Blok | Sesi A dan Sesi B | Email | Env password |
|---|---|---|---|
| TC-AC-ACC-187 | Total Control (Principal) A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `AC_TC_PASSWORD` |
| TC-AC-ACC-961 | Active-Delete-Only A-07 | `activeDeleteJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_DELETE_PASSWORD` |

- Sesi A login di hook `before` spec ini (Total Control); halaman Admin Console > Client dibuka hook `beforeEach` suite; Sesi B login lewat langkah eksplisit; hook `after` mengembalikan kedua sesi ke akun default suite (Total Control).
- Kemampuan teknis (sesi): Sesi B memakai akun yang sama tanpa mengusir Sesi A (suite.md > Kemampuan teknis > Dua sesi web akun yang sama).
- Data Pre-setup/A3: C-13 `PT Ganti Mitra` (hanya CV Mitra Sejati; "CV Mitra Lestari" ditambah oleh Sesi A lalu di-Remove untuk pemulihan; relasi "CV Mitra Lestari" menjadi `transferred`, baris Changelog dan Last Updated bertambah); C-W3LIF-1 `PT Hapus Dua Sesi` (Active, Direct, Group Area Jakarta, Client Code `W3L-001`, belum pernah memiliki subscription, Default User Not Yet Activated email `hapusduasesi@qwertysystem.net`, tanpa user ber-App Access; kelas Dikonsumsi). Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang kedua Client di hook `before` dan `after`. Partner pembanding: `CV Mitra Lestari`, `CV Mitra Mandiri`.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-187: Dua admin mengubah relasi Partner bersamaan: Sesi B menerima dialog konflik 409

1. [Sesi B] Login sebagai Total Control A-01 di konteks kedua dan buka Admin Console > Client
2. [Sesi A dan Sesi B] Ketik Search `PT Ganti Mitra`, tekan Enter, klik `[⋯]` pada baris `PT Ganti Mitra` → klik `Change Partner`
3. [Sesi A] Klik `[+ Add Partner]`, pilih "CV Mitra Lestari", lalu klik `[Confirm]`
4. [Sesi A] Verifikasi toast sukses "Success, partner has been updated."
5. [Sesi B] Klik `[+ Add Partner]`, pilih "CV Mitra Mandiri", lalu klik `[Confirm]`
6. [Sesi B] Verifikasi dialog konflik tampil tanpa Title
7. [Sesi B] Verifikasi dialog konflik berisi pesan "This client was changed by someone else. Please review."
8. [Sesi B] Verifikasi footer dialog konflik berupa `[OK]`
9. [Sesi B] Verifikasi toast sukses tidak tampil
10. [Sesi B] Klik `[OK]`
11. [Sesi B] Verifikasi dialog Change Partner tertutup
12. [Sesi B] Muat ulang Admin Console > Client, ketik Search `PT Ganti Mitra`, tekan Enter, klik `[⋯]` pada baris `PT Ganti Mitra` → klik `Change Partner`
13. [Sesi B] Verifikasi list "Current Partners" memuat "CV Mitra Sejati" dan "CV Mitra Lestari", masing-masing berbadge `Active`
14. [Sesi B] Verifikasi list "Current Partners" tidak memuat "CV Mitra Mandiri"
15. [Sesi B] Klik `[✕]` pada dialog Change Partner
16. [Sesi B] Ketik Search `PT Ganti Mitra`, tekan Enter, klik `[⋯]` pada baris `PT Ganti Mitra` → klik `Change Partner`, klik `[Remove]` pada "CV Mitra Lestari", lalu klik `[Confirm]`
17. [Sesi B] Tunggu aksi selesai (dialog Change Partner tertutup)
18. Tutup konteks Sesi B dan hapus sesi login-nya

### Blok Active-Delete-Only

19. Ganti akun: pada Sesi A, logout lalu login sebagai Active-Delete-Only A-07; buka Sesi B di konteks kedua dan login sebagai Active-Delete-Only A-07

#### TC-AC-ACC-961: Delete Client yang sudah dihapus sesi lain sebelum Confirm: sukses tanpa error dan tanpa baris Changelog baru

20. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Hapus Dua Sesi` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Delete` (N1), lalu tutup modal
21. [Sesi A] Klik sub-tab Active, ketik Search `PT Hapus Dua Sesi`, tekan Enter
22. [Sesi A] Klik `[⋯]` pada baris `PT Hapus Dua Sesi` → klik `Delete`, ketik nama persis pada input "Type the client name to confirm", dan centang "I understand this action cannot be undone" (dialog tetap terbuka)
23. [Sesi B] Klik sub-tab Active, ketik Search `PT Hapus Dua Sesi`, tekan Enter, klik `[⋯]` pada baris tersebut → klik `Delete`, ketik nama persis, centang checkbox, lalu klik `[Delete]`
24. [Sesi B] Verifikasi toast sukses "Success, client has been deleted."
25. [Sesi A] Klik `[Delete]` pada dialog
26. [Sesi A] Verifikasi toast sukses "Success, client has been deleted."
27. [Sesi A] Verifikasi tidak ada toast error
28. [Sesi A] Verifikasi dialog Delete tertutup
29. [Sesi A] Verifikasi Sesi A kembali ke List sub-tab Active
30. [Sesi A] Ketik Search `PT Hapus Dua Sesi` di Search List, tekan Enter
31. [Sesi A] Verifikasi baris `PT Hapus Dua Sesi` tidak tampil di sub-tab Active
32. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Hapus Dua Sesi` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Delete` (N2)
33. [Sesi A] Verifikasi N2 adalah N1 + 1 (satu baris `Delete` dari Sesi B; Sesi A tidak menambah baris)
34. Tutup konteks Sesi B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah. Awalan `[Sesi A]` dan `[Sesi B]` menandai konteks.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas dua TC satu jenis harness (dua sesi admin yang kedua-duanya diasersi); tiap blok memakai Client dan pasangan akun sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Ganti akun lewat Step eksplisit (langkah 19) sah karena bagian sesudahnya tetap bermakna.
- Langkah penghubung (tanpa awalan Verifikasi): pemulihan Partner (langkah 15 dan 16; Post Condition TC-AC-ACC-187), "Tunggu aksi selesai" sesudah pemulihan (langkah 17; butir 8 bagian 8b), penutupan konteks Sesi B (langkah 18 dan 34; S-09), ganti akun (langkah 19), dan Search yang menemukan baris target (R-16). Asersi absence baris pada langkah 31 berlandaskan toast sukses Delete (langkah 26) sebagai anchor positif (bagian 8b butir 2).
- Post Condition TC-AC-ACC-961 ("Seed ulang C-W3LIF-1") dilakukan di hook.
- Temuan untuk QA:
  - TC-AC-ACC-187 Manual Only "dua sesi paralel": kebutuhan dua konteks UI dicatat di Prerequisites; Sesi B login Total Control yang sama dengan Sesi A.
  - TC-AC-ACC-961 Expected b menyatakan toast sukses di Sesi A tanpa toast error; hasil server (idempoten bila Client sudah terhapus) tidak dijelaskan lebih lanjut oleh TC.
