---
id: TC-AC-ACC-E2E-151-delete-diblok-subscription-ditambahkan-sesi-lain
title: "Delete Diblok D-03 dan D-14 karena Subscription Ditambahkan Sesi Lain Tepat Sebelum Confirm (Archived, Active, dan Suspended)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-222
  - TC-AC-ACC-225
  - TC-AC-ACC-982
coverage:
  web: automated
---

# Delete Diblok D-03 dan D-14 karena Subscription Ditambahkan Sesi Lain Tepat Sebelum Confirm (Archived, Active, dan Suspended)

## Prerequisites

- Mode: FE+BE.
- Konteks (kelas c, dua sesi): Sesi A (UI, diasersi) dan Sesi B (menambah subscription).
- Akun aktor (urutan blok = urutan akun):

| Blok | Sesi A | Email | Env password | Sesi B | TC |
|---|---|---|---|---|---|
| 1 | Archived-Delete-Only A-10 | `archivedDeleteJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ARCHIVED_DELETE_PASSWORD` | Total Control (Principal) A-01 (`AC_TC_PASSWORD`) | 222 |
| 2 | Total Control A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `AC_TC_PASSWORD` | Total Control A-01 | 225, 982 |

- Sesi A login di hook `before` spec ini (Archived-Delete-Only); halaman Admin Console > Client dibuka hook `beforeEach` suite; Ganti akun ke Total Control lewat Step eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Sesi B (UI): konteks kedua (browser kedua) yang login sebagai Total Control A-01 dan mengoperasikan Admin Console > Client Subscription untuk menambah subscription. Kedua sesi dikendalikan oleh peran Total Control yang sama; sesi UI kedua dipakai karena TC menyebut aksi lewat Admin Console > Client Subscription (alur dimiliki modul Client Subscription).
- Kemampuan teknis (sesi): Sesi B memakai akun yang sama tanpa mengusir Sesi A (suite.md > Kemampuan teknis > Dua sesi web akun yang sama).
- Data (kelas Dikonsumsi; Fixture BE yang disediakan tim FE/BE, idempotent, men-seed ulang tanpa syarat di hook `before` dan `after`): C-05 `PT Lama Tak Berbayar` (Archived; FAMS Purge, SAMS Deleted; term baru Active tersisa setelah TC-AC-ACC-222); C-09 `PT Baru Daftar` (Active, belum pernah berlangganan; term baru Pending tersisa setelah TC-AC-ACC-225); C-FX12-7 `PT Suspend Race Term` (Suspended, belum pernah berlangganan; term Active tersisa setelah TC-AC-ACC-982).
- Subscription yang ditambahkan Sesi B: FAMS mode New yang terotorisasi langsung. Untuk `PT Lama Tak Berbayar`: terotorisasi langsung. Untuk `PT Baru Daftar`: tanggal mulai di masa depan sehingga term berstatus Pending. Untuk `PT Suspend Race Term`: Plan Professional, Duration 1 year(s), Start Date hari ini sehingga term berstatus Active.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-222: Dialog blok D-03: subscription Active ditambahkan sesi lain tepat sebelum Confirm Delete

1. [Sesi B] Login sebagai Total Control A-01 di konteks kedua
2. [Sesi A] Klik sub-tab Archived, ketik Search `PT Lama Tak Berbayar`, tekan Enter
3. [Sesi A] Klik `[⋯]` pada baris `PT Lama Tak Berbayar` → klik `Delete`, ketik nama persis dan centang checkbox
4. [Sesi B] Buka Admin Console > Client Subscription dan tambah subscription FAMS mode New yang terotorisasi langsung untuk `PT Lama Tak Berbayar`
5. [Sesi A] Klik `[Delete]`
6. [Sesi A] Verifikasi dialog blok Title "Cannot Delete Client" dengan bullet `• PT Lama Tak Berbayar`
7. [Sesi A] Verifikasi dialog blok memuat "This client still has active or expiring subscriptions. Cancel all subscriptions before deleting."
8. [Sesi A] Verifikasi dialog blok memuat tombol `[OK]` dengan lebar 480px
9. [Sesi A] Klik `[OK]`
10. [Sesi A] Verifikasi Client `PT Lama Tak Berbayar` tidak terhapus (baris tetap tampil di sub-tab Archived)
11. Tutup konteks Sesi B dan hapus sesi login-nya

### Blok Total Control

12. Ganti akun: pada Sesi A, logout lalu login sebagai Total Control A-01; buka Sesi B di konteks kedua dan login sebagai Total Control A-01

#### TC-AC-ACC-225: Delete Active/Suspended: term Pending ditambahkan sesi lain tepat sebelum Confirm diblok D-14

13. [Sesi A] Ketik Search `PT Baru Daftar`, tekan Enter
14. [Sesi A] Klik `[⋯]` pada baris `PT Baru Daftar` → klik `Delete`, ketik nama persis dan centang checkbox
15. [Sesi B] Buka Admin Console > Client Subscription dan tambah subscription FAMS mode New yang terotorisasi langsung untuk `PT Baru Daftar` dengan tanggal mulai di masa depan sehingga term berstatus Pending
16. [Sesi A] Klik `[Delete]`
17. [Sesi A] Verifikasi dialog blok Title "Cannot Delete Client" dengan bullet `• PT Baru Daftar`
18. [Sesi A] Verifikasi dialog blok memuat "This client still has a subscription request in progress."
19. [Sesi A] Verifikasi dialog blok memuat tombol `[OK]` dengan lebar 480px
20. [Sesi A] Klik `[OK]`
21. [Sesi A] Verifikasi Client `PT Baru Daftar` tidak terhapus (baris tetap tampil)

#### TC-AC-ACC-982: Delete Client Suspended: subscription Active ditambahkan sesi lain tepat sebelum Confirm diblok D-03 (bukan toast 403 baku)

22. [Sesi A] Klik sub-tab Suspended, ketik Search `PT Suspend Race Term`, tekan Enter
23. [Sesi A] Klik `[⋯]` pada baris `PT Suspend Race Term` → klik `Delete`, ketik nama persis dan centang checkbox
24. [Sesi B] Buka Admin Console > Client Subscription dan tambah subscription FAMS mode New yang terotorisasi langsung untuk `PT Suspend Race Term` (Plan Professional, Duration 1 year(s), Start Date hari ini) sehingga term berstatus Active
25. [Sesi A] Klik `[Delete]`
26. [Sesi A] Verifikasi dialog blok Title "Cannot Delete Client" dengan bullet `• PT Suspend Race Term`
27. [Sesi A] Verifikasi dialog blok memuat "This client still has active or expiring subscriptions. Cancel all subscriptions before deleting."
28. [Sesi A] Verifikasi dialog blok memuat tombol `[OK]`
29. [Sesi A] Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tidak tampil
30. [Sesi A] Klik `[OK]`
31. [Sesi A] Ganti isi Search dengan `PT Suspend Race Term`, tekan Enter
32. [Sesi A] Verifikasi baris `PT Suspend Race Term` tetap tampil di sub-tab Suspended
33. Tutup konteks Sesi B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah. Awalan `[Sesi A]` dan `[Sesi B]` menandai konteks. Sesi B adalah konteks UI kedua karena TC menyebut alur lewat Admin Console > Client Subscription (modul lain).
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas tiga TC satu topik dan satu jenis harness (dua sesi, blok D-03/D-14 karena kondisi data dibuat oleh sesi lain); tiap blok memakai Client sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Ganti akun lewat Step eksplisit (langkah 12) sah karena bagian sesudahnya tetap bermakna.
- Langkah penghubung (tanpa awalan Verifikasi): penutupan konteks Sesi B (langkah 11 dan 33; S-09), ganti akun (langkah 12), klik `[OK]` penutup dialog blok (langkah 9, 20, 30), dan Search yang menemukan baris target (R-16). Asersi "Client tidak terhapus" (langkah 10, 21, 32) memakai hasil Search sebagai anchor positif.
- Post Condition TC-AC-ACC-222, 225, 982 ("Seed ulang ...") dilakukan di hook.
- Temuan untuk QA:
  - TC-AC-ACC-222 Expected a/b tidak menyebut observasi "Client tidak terhapus" selain Expected; spec mengasersinya lewat Search pada langkah 10.
  - TC-AC-ACC-225 Expected b dan TC-AC-ACC-982 Expected b ("Client tidak terhapus") tidak menyebut cara observasi pada TC-AC-ACC-225; spec memakai baris yang tampil di List.
  - TC-AC-ACC-225 Precondition b menyebut Sesi B Total Control (Principal) tanpa akun terpisah; spec memakai akun yang sama dengan Sesi A.
