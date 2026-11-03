---
id: TC-AC-PF-E2E-175-tab-assigned-clients-empty-state-navigasi-client-detail
title: "Tab Assigned Clients: empty state, subscription baru dari Allocation, dan navigasi ke Client Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-451
  - TC-AC-PF-552
  - TC-AC-PF-611
  - TC-AC-PF-783
coverage:
  web: automated
---

# Tab Assigned Clients: empty state, subscription baru dari Allocation, dan navigasi ke Client Detail

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`. Akun yang sama dapat membuka Allocation > Client Subscription (precondition TC-AC-PF-611).
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D dan custom plan `Paket Tanpa Client` ke keadaan awal secara idempoten, termasuk menghapus subscription `PT Baru Aktif` yang dibuat spec ini di hook `before` dan `after`. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup (pengecualian S-06/S-12 butir A-14: nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`):
  - Custom plan `Paket Tanpa Client` tersedia tanpa client dan tanpa subscription.
  - Dataset Plan D, default plan `Growth` v5 dengan 9 client, termasuk `PT Sejahtera Abadi` Active v5 17 Jun 26 John Doe.
- Data Dinamis: subscription Active untuk `PT Baru Aktif` dengan plan `Paket Tanpa Client`, dibuat langkah 9 lewat Allocation > Client Subscription; hook `after` menghapusnya lewat fixture backend. Pada Plans List, efeknya adalah kolom Clients `Paket Tanpa Client` berubah dari `0` menjadi `1`; Last Updated plan tidak diasersi.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: subscription `PT Baru Aktif` dihapus di hook `after`; Last Updated dan Changelog plan tidak diasersi. Suite berjalan serial (`parallel: false`).

## Test Steps

### Empty state genuinely kosong (TC-AC-PF-451)

1. Klik tab `Custom`, sub-tab `Active`.
2. Buka Plan Detail `Paket Tanpa Client` (klik nama plan `Paket Tanpa Client`).
3. Klik Tab Assigned Clients.
4. Verifikasi area tabel menampilkan Illustration, Title "No assigned clients yet", dan Description "Clients assigned to this plan will appear here.".
5. Verifikasi area tabel tidak memuat tombol CTA.
6. Verifikasi teks jumlah client outdated tidak tampil.

### Subscription baru dari Allocation (TC-AC-PF-611)

7. Kembali ke Plans & Licensing > Plans & Features > Custom > Active.
8. Verifikasi kolom Clients baris `Paket Tanpa Client` bernilai `0`.
9. Buka Allocation > Client Subscription → `+ Subscription` dan buat subscription berstatus Active untuk `PT Baru Aktif` dengan plan `Paket Tanpa Client`.
10. Tunggu aksi selesai (dialog atau form `+ Subscription` tertutup dan daftar Client Subscription kembali tampil).
11. Kembali ke Plans & Licensing > Plans & Features > Custom > Active dan muat ulang halaman.
12. Verifikasi kolom Clients baris `Paket Tanpa Client` bernilai `1`.
13. Buka Plan Detail `Paket Tanpa Client`.
14. Klik Tab Assigned Clients.
15. Verifikasi Tab Assigned Clients memuat baris `PT Baru Aktif` berstatus `Active`.
16. Verifikasi baris `PT Baru Aktif` memuat Plan Version versi terbaru.
17. Verifikasi baris `PT Baru Aktif` tidak memuat badge `Outdated`.

### Navigasi ke Client Detail dan Back (TC-AC-PF-552 dan TC-AC-PF-783)

18. Kembali ke Plans & Licensing > Plans & Features > Default > Active.
19. Buka Plan Detail `Growth`.
20. Klik Tab Assigned Clients.
21. Klik link `PT Sejahtera Abadi` pada kolom Client Name.
22. Verifikasi Client Detail `PT Sejahtera Abadi` terbuka pada tab yang sama.
23. Klik tombol Back browser.
24. Verifikasi Plan Detail `Growth` tampil kembali dengan Tab Assigned Clients aktif (bukan Tab Overview).
25. Buka Overlay Row Action `PT Sejahtera Abadi` → `Detail`.
26. Verifikasi Client Detail `PT Sejahtera Abadi` terbuka pada tab yang sama.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 7, 11, dan 18 (berpindah antar halaman), 10 (menunggu aksi pembuatan subscription selesai sebelum berpindah surface, bagian 8b butir 8), serta 13 (membuka Plan Detail setelah muat ulang).
- Langkah 23 dan 24 dipakai bersama oleh TC-AC-PF-552 (langkah "Kembali" sebelum membuka Overlay Row Action) dan TC-AC-PF-783 (Back dari Client Detail); satu perjalanan menjalankan keduanya sesuai urutan langkah masing-masing TC.
- Urutan TC dalam spec: TC-AC-PF-451 (plan tanpa client) ditulis sebelum TC-AC-PF-611 karena TC-AC-PF-611 menambah subscription ke plan yang sama dan mengakhiri kondisi "tanpa client".
- Temuan untuk QA:
  - TC-AC-PF-611 ("buat subscription berstatus Active untuk `PT Baru Aktif`") tidak menyebut field form `+ Subscription` yang diisi (term, tanggal, dan sebagainya); spec menyalin langkahnya apa adanya dan memerlukan rincian dari tim FE atau TC Allocation.
  - Judul TC-AC-PF-611 menyebut "tanpa Push Update", tetapi langkah dan Expected tidak memuat asersi Push Update; tidak diasersi.
  - Post Condition TC-AC-PF-611 ("Subscription `PT Baru Aktif` aktif pada plan") tidak punya langkah observasi sendiri di luar Expected c; tidak diasersi terpisah.
  - Pada TC-AC-PF-552 dan TC-AC-PF-783 Expected tidak menyebut Back mengembalikan state Tab Assigned Clients selain "bukan Tab Overview"; keduanya diasersi seperti tertulis.
