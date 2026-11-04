---
id: TC-FA-LBL-E2E-006-role-matrix-visibilitas-aksi-katalog-label-per-role
title: "Role Matrix: visibilitas aksi katalog Labels per role"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB-LOGIC-05a
coverage:
  web: automated
---

# Role Matrix: visibilitas aksi katalog Labels per role

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke `DU-01`.
- Role yang diuji (akun hanya lewat env, tidak ada password di spec):

| Role | Data | Env email | Env password | Create | Edit | Delete |
|---|---|---|---|---|---|---|
| Total Control | `DU-01` | `FA_TC_EMAIL` | `FA_TC_PASSWORD` | tampil | tampil | tampil |
| Read Only | `DU-02` | `FA_RO_EMAIL` | `FA_RO_PASSWORD` | Hidden | Hidden | Hidden |
| Create Only (Permission Create pada "Manage Asset Master Data") | `DU-03` | `FA_CO_EMAIL` | `FA_CO_PASSWORD` | tampil | Hidden | Hidden |
| Update Only (Permission Update pada "Manage Asset Master Data") | `DU-04` | `FA_UO_EMAIL` | `FA_UO_PASSWORD` | Hidden | tampil | Hidden |
| Delete Only (Permission Delete pada "Manage Asset Master Data") | `DU-05` | `FA_DO_EMAIL` | `FA_DO_PASSWORD` | Hidden | Hidden | tampil |
| Role Lain tanpa capability | `DU-06` | `FA_NOROLE_EMAIL` | `FA_NOROLE_PASSWORD` | tab Labels Hidden | tab Labels Hidden | tab Labels Hidden |

- Data uji: `DU-18` (label seed milik spec, bersuffix `{runId}-006`, warna `#3B82F6`, dibuat lewat API di hook `before` dan dihapus di hook `after`).
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, disediakan tim FE/BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB-LOGIC-05a: Gerbang Global Role "Manage Asset Master Data" atas Create, Edit, dan Delete katalog Labels

1. Ketik Search `DU-18`, tekan Enter
2. Verifikasi baris label `DU-18` tampil pada Labels List
3. Verifikasi tombol `[+ Label]` tampil pada Table Tools
4. Klik `[⋯]` pada baris label `DU-18`
5. Verifikasi aksi `Edit` dan `Delete` tampil pada menu `[⋯]`
6. Ganti akun ke Read Only: logout, login dengan akun `DU-02`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
7. Ketik Search `DU-18`, tekan Enter
8. Verifikasi baris label `DU-18` tampil pada Labels List
9. Verifikasi tombol Download dan ikon Changelog tampil pada Table Tools
10. Verifikasi tombol `[+ Label]` tidak tampil pada Table Tools
11. Klik `[⋯]` pada baris label `DU-18`
12. Verifikasi aksi `Detail` tampil pada menu `[⋯]`
13. Verifikasi aksi `Edit` dan `Delete` tidak tampil pada menu `[⋯]`
14. Ganti akun ke Create Only: logout, login dengan akun `DU-03`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
15. Ketik Search `DU-18`, tekan Enter
16. Verifikasi baris label `DU-18` tampil pada Labels List
17. Verifikasi tombol `[+ Label]` tampil pada Table Tools
18. Klik `[⋯]` pada baris label `DU-18`
19. Verifikasi aksi `Detail` tampil pada menu `[⋯]`
20. Verifikasi aksi `Edit` dan `Delete` tidak tampil pada menu `[⋯]`
21. Ganti akun ke Update Only: logout, login dengan akun `DU-04`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
22. Ketik Search `DU-18`, tekan Enter
23. Verifikasi baris label `DU-18` tampil pada Labels List
24. Verifikasi tombol Download dan ikon Changelog tampil pada Table Tools
25. Verifikasi tombol `[+ Label]` tidak tampil pada Table Tools
26. Klik `[⋯]` pada baris label `DU-18`
27. Verifikasi aksi `Detail` tampil pada menu `[⋯]`
28. Verifikasi aksi `Edit` tampil pada menu `[⋯]`
29. Verifikasi aksi `Delete` tidak tampil pada menu `[⋯]`
30. Ganti akun ke Delete Only: logout, login dengan akun `DU-05`, lalu buka Fixed Asset > Settings > Asset Master > tab Labels
31. Ketik Search `DU-18`, tekan Enter
32. Verifikasi baris label `DU-18` tampil pada Labels List
33. Verifikasi tombol Download dan ikon Changelog tampil pada Table Tools
34. Verifikasi tombol `[+ Label]` tidak tampil pada Table Tools
35. Klik `[⋯]` pada baris label `DU-18`
36. Verifikasi aksi `Detail` tampil pada menu `[⋯]`
37. Verifikasi aksi `Delete` tampil pada menu `[⋯]`
38. Verifikasi aksi `Edit` tidak tampil pada menu `[⋯]`
39. Ganti akun ke Role Lain tanpa capability: logout, login dengan akun `DU-06`, lalu buka Fixed Asset > Settings > Asset Master
40. Verifikasi tab `Labels` tidak tampil pada halaman Settings > Asset Master yang termuat

## Notes

- Langkah penghubung: Search `DU-18` (langkah 1, 7, 15, 22, 31) menemukan baris target di Labels List yang dapat memuat lebih dari satu halaman; klik `[⋯]` membuka menu baris; langkah ganti akun (6, 14, 21, 30, 39) berupa langkah eksplisit tanpa `Verifikasi` karena akun pertama login di hook `before`.
- Spec ditulis per blok role dengan ganti akun eksplisit (konvensi bagian 3a): pola langkah tiap role identik, hasil per role berbeda, dan Total Control login di hook `before`.
- Anchor absence: baris label `DU-18` tampil pada Labels List (langkah 8, 16, 23, 32) dan tombol Download serta ikon Changelog tampil pada Table Tools (langkah 9, 24, 33; PRD §2.1 dan §5: Download Export untuk keempat role dan Download serta Changelog "Selalu berlaku") mendahului asersi `Hidden` untuk `[+ Label]`; aksi `Detail` tampil pada menu `[⋯]` (langkah 12, 19, 27, 36; PRD §4.7 dan §2.1: View Tagged Assets) mendahului asersi `Edit` dan `Delete` tidak tampil; `Edit` tampil (langkah 28) dan `Delete` tampil (langkah 37) menjadi anchor untuk asersi pasangannya.
- Alasan spec melewati 35 langkah: enam blok role satu kelas harness (Role Matrix) dengan pola langkah yang sama dan tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan pemecahan menambah login dan seeding `DU-18` per spec.
- Pembagian klausa lintas spec: `FALB-LOGIC-05a` dikutip spec 005, 006, dan 007. Spec 005 mengasersi penolakan server atas Create dari request langsung oleh Read Only; spec ini mengasersi visibilitas `[+ Label]`, `Edit`, dan `Delete` di UI per role; spec 007 mengasersi akun `DU-19` memiliki aksi katalog dan akun `DU-20` tidak memiliki tab `Labels`.
- Temuan PRD: matriks §2.1 dan §4.7 tidak ber-ID per sel sehingga tiap kombinasi role × aksi tidak dapat dikutip sebagai aturan sendiri; sel matriks `FALB-LOGIC-05a` untuk Akses Tab Labels (selain `DU-06`), baris Default User dan Group Manager, serta visibilitas kolom checkbox dan Bulk Action Bar (§4.7) tidak diasersi. Download Export dan View Tagged Assets dipakai hanya sebagai anchor (langkah 9, 12, 19, 24, 27, 33, dan 36).
- Temuan PRD: PRD tidak menyatakan apa yang tampil bila Role Lain membuka Settings > Asset Master dan tidak menyatakan elemen yang pasti tampil di halaman itu (tab `Asset Name` juga dinaungi "Manage Asset Master Data"), sehingga asersi tab `Labels` tidak tampil (langkah 40) tidak punya anchor positif yang dinyatakan PRD; asersi tetap dipertahankan dan halaman Settings > Asset Master yang termuat menjadi satu-satunya anchor permukaan.
