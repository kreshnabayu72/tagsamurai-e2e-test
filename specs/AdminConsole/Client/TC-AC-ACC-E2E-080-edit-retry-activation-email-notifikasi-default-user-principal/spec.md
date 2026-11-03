---
id: TC-AC-ACC-E2E-080-edit-retry-activation-email-notifikasi-default-user-principal
title: "Notifikasi Kegagalan Activation Email Diterima Default User Principal Setelah Percobaan Ulang Ketiga"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-973
coverage:
  web: automated
---

# Notifikasi Kegagalan Activation Email Diterima Default User Principal Setelah Percobaan Ulang Ketiga

## Prerequisites

- Mode: FE+BE. Kelas harness eksternal (majukan waktu sistem, antrean percobaan ulang).
- Akun aktor: Default User (Principal) (A-ROL-3) `defaultUserPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_DU_PRINCIPAL_PASSWORD`. Login akun Default User (Principal) di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Kemampuan teknis: memajukan waktu sistem (jam server) dan memicu antrean percobaan ulang berjalan; jam browser tidak diubah karena antrean percobaan ulang dihitung di server dan tidak diamati lewat countdown UI (bagian 6 konvensi); jam server dipulihkan ke waktu nyata di hook `after` dan sebelum membuka Activity Log atau Changelog (S-09). Memaksa email service gagal (5xx) pada setiap percobaan kirim (disediakan tim FE/BE; endpoint tidak dikarang). Membaca jumlah notifikasi berstatus Unread dan item teratas pada dropdown notifikasi navbar.
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- Dataset seed (nama bersuffix): Client `PT Notif Default User {runId}-080` (replika C-FX10-3: Active, FAMS Active, Default User Not Yet Activated, Email awal `notifdefaultuser.awal+{runId}-080@qwertysystem.net`). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Jeda percobaan ulang otomatis: 1 menit, 5 menit, 15 menit.
- Cleanup: hook `after` membatalkan simulasi kegagalan email service, men-seed ulang Client dengan Email awal, menandai notifikasi uji `[Mark as Read]`, dan memulihkan waktu sistem.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi Unread (N1), lalu tutup dropdown
2. Paksa email service gagal pada setiap percobaan kirim (5xx)
3. Klik sub-tab Active
4. Ketik Search `PT Notif Default User {runId}-080`, tekan Enter
5. Buka `⋯` baris `PT Notif Default User {runId}-080` lalu klik `Edit`
6. Ubah Email Default User menjadi `notifdefaultuser.baru+{runId}-080@qwertysystem.net`
7. Klik `[Save]`
8. Verifikasi toast sukses "Success, client has been updated."
9. Majukan waktu sistem 1 menit dan tunggu antrean percobaan ulang berjalan
10. Buka dropdown notifikasi, catat jumlah Unread (N2), lalu tutup dropdown
11. Verifikasi N2 sama dengan N1
12. Majukan waktu sistem 5 menit dan tunggu antrean percobaan ulang berjalan
13. Buka dropdown notifikasi, catat jumlah Unread (N3), lalu tutup dropdown
14. Verifikasi N3 sama dengan N1
15. Majukan waktu sistem 15 menit dan tunggu antrean percobaan ulang berjalan
16. Buka dropdown notifikasi, catat jumlah Unread (N4), dan lihat item teratas
17. Verifikasi N4 sama dengan N1 + 1
18. Verifikasi item teratas berstatus Unread dengan Title "Activation email not delivered" dan Body "PT Notif Default User {runId}-080: the activation email could not be sent after repeated attempts."
19. Verifikasi tombol aksi item teratas hanya `[Mark as Read]` (tidak ada `[Detail]`)
20. Klik `[Mark as Read]` pada notifikasi uji lalu pulihkan waktu sistem ke waktu nyata

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): pencatatan N, Search nama unik, `[Mark as Read]` dan pemulihan waktu.
- Temuan untuk QA:
  - TC-973 bertanda Manual Only (memajukan waktu sistem).
