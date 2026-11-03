---
id: TC-AC-ACC-E2E-131-defense-client-suspended-dan-archived-request-langsung
title: "Defense-in-depth: Aksi Tulis pada Client Suspended dan Archived Hidden di UI dan Request Langsung Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-183
  - TC-AC-ACC-907
  - TC-AC-ACC-906
  - TC-AC-ACC-170
  - TC-AC-ACC-253
coverage:
  web: automated
---

# Defense-in-depth: Aksi Tulis pada Client Suspended dan Archived Hidden di UI dan Request Langsung Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun, Step ganti akun eksplisit):
  - Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD` (TC-AC-ACC-183, 907, 906). Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD` (TC-AC-ACC-170, 253).
  - Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga data tidak berubah): C-03 `PT Wahana Nusantara` (Suspended); C-AST-6 `PT Arsip Belum Aktif` (Archived, semua term Archive, Default User Not Yet Activated, toggle BYO Disabled); C-AST-5 `PT Suspend Belum Aktif` (Suspended, FAMS Active, Default User Not Yet Activated, toggle BYO Disabled). Partner pembanding: `CV Mitra Lestari`.
- Kemampuan teknis (kelas a): klien HTTP yang mengirim request langsung ke server (tanpa melalui browser) memakai sesi API aktor yang sedang login (`suite.md` > Kemampuan teknis > Sesi API aktor; token sesi aktor, tidak dihitung sebagai sesi web; kemampuan disediakan tim FE/BE), dengan asersi kode respons 403; membaca nilai toggle BYO dan jumlah email lewat Fixture BE/mail-catcher (disediakan tim FE/BE). Alamat email Default User C-AST-6 tidak tertulis di Tabel A3 (lihat Temuan).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-183: Change Partner pada Client Suspended: aksi Hidden dan request langsung ditolak server dengan respons 403

1. Klik sub-tab Suspended
2. Ketik Search `PT Wahana Nusantara`, tekan Enter
3. Klik `[⋯]` pada baris `PT Wahana Nusantara`
4. Verifikasi menu `[⋯]` `PT Wahana Nusantara` tidak memuat `Change Partner`
5. Kirim request Change Partner langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Wahana Nusantara` dengan menambahkan Partner "CV Mitra Lestari"
6. Verifikasi respons server 403 Forbidden

### TC-AC-ACC-907: Client Archived: [Resend Activation Email] Hidden dan request langsung ditolak server

7. Klik breadcrumb "Client"
8. Klik sub-tab Archived, ketik Search `PT Arsip Belum Aktif`, tekan Enter, klik Company Name `PT Arsip Belum Aktif`
9. Lihat Section "Default User"
10. Verifikasi badge Default User "Not Yet Activated" tampil
11. Verifikasi `[Resend Activation Email]` Hidden
12. Catat jumlah email aktivasi di inbox Default User `PT Arsip Belum Aktif` (E0)
13. Kirim request Resend Activation Email langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Arsip Belum Aktif`
14. Verifikasi respons server 403 Forbidden
15. Verifikasi jumlah email aktivasi di inbox Default User tetap E0 (tidak ada email terkirim)

### TC-AC-ACC-906: Client Archived: toggle BYO Hidden dan request langsung ditolak server

16. Lihat Section "Settings" pada Detail `PT Arsip Belum Aktif`
17. Verifikasi toggle "Allow Self-Purchased Device Activation" Hidden pada Section "Settings"
18. Kirim request set "Allow Self-Purchased Device Activation" ke Enabled langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Arsip Belum Aktif`
19. Verifikasi respons server 403 Forbidden
20. Verifikasi nilai toggle `PT Arsip Belum Aktif` tetap Disabled

### Blok Active-Full

21. Ganti akun: logout lalu login sebagai Active-Full A-15

#### TC-AC-ACC-170: Client Suspended: [Resend Activation Email] Hidden dan request langsung ditolak server dengan respons 403

22. Klik sub-tab Suspended, ketik Search `PT Suspend Belum Aktif`, tekan Enter, klik Company Name `PT Suspend Belum Aktif`
23. Lihat Section "Default User"
24. Verifikasi badge Default User "Not Yet Activated" tampil
25. Verifikasi `[Resend Activation Email]` Hidden
26. Kirim request Resend Activation Email langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Suspend Belum Aktif`
27. Verifikasi respons server 403 Forbidden

#### TC-AC-ACC-253: Client Suspended: toggle BYO Hidden dan request langsung ditolak server dengan respons 403

28. Lihat Section "Settings" pada Detail `PT Suspend Belum Aktif`
29. Verifikasi toggle "Allow Self-Purchased Device Activation" Hidden pada Section "Settings"
30. Kirim request set "Allow Self-Purchased Device Activation" ke Enabled langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Suspend Belum Aktif`
31. Verifikasi respons server 403 Forbidden

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: kelima TC adalah kelas a (defense-in-depth) dengan Expected berupa respons API dan state data; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md`. Request langsung dikirim lewat klien HTTP tanpa melalui browser, sehingga asersi hanya kode respons (403 Forbidden) dan state data (bagian 8b butir 1); Expected kelima TC memang hanya memuat respons HTTP tanpa toast atau dialog.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 1 sampai 3 dan 7 sampai 9 (navigasi ke baris/Detail target), langkah 21 (ganti akun), dan Search yang menemukan baris target (R-16). Langkah 12 adalah baseline jumlah email (R-11).
- Post Condition TC-AC-ACC-183, 907, 906, 170, 253: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-907 Expected b ("tidak ada email terkirim") tidak menyebut alamat email Default User `PT Arsip Belum Aktif` dan tidak memberi cara observasi; spec memakai baseline mail-catcher (R-11) dengan alamat yang disediakan fixture.
