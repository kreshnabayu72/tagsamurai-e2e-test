---
id: TC-AC-LA-E2E-138-approve-approver-entitas-berbeda-activity-log
title: "Approve oleh Approver Entitas Berbeda dari Plan Owner: Satu Entri Activity Log di Dua Entitas dan Changelog Tidak Bertambah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-517
coverage:
  web: automated
---

# Approve oleh Approver Entitas Berbeda dari Plan Owner: Satu Entri Activity Log di Dua Entitas dan Changelog Tidak Bertambah

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Hendra Wijaya (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Ganti akun ke Fajar Nugroho dilakukan eksplisit pada langkah 14 dan 15; hook `after` mengembalikan sesi ke akun default suite. Flag Guided Tooltip diatur hook `before` suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Hendra Wijaya | #1 | Total Control Principal (approver, entitas Principal PT ABC) | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` |
| Fajar Nugroho | #10 | Total Control Distributor, staf Plan Owner PT Maju Bersama | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Require Approval for Allocation ON (Pre-setup #38), data Changelog seed (Pre-setup #54: 25 entri) sebagai pembanding.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #60 bersama): `{idFree}`, alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester `Sari P` (Default User Principal, Pre-setup #2), Payment Free tanpa Reserve (bentuk Pre-setup #60).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; kemampuan membaca jumlah entri Changelog modul (`{nChangelog}`), dicatat di hook `before` setelah seeding dan sebelum Approve.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > License Allocation
2. Klik `[Review]` pada alokasi `{idFree}` milik `Sari P`
3. Pilih Approve
4. Klik Submit
5. Tunggu aksi selesai (tombol Submit aktif kembali atau baris keputusan hilang dari Tab Active)
6. Buka Activity Log Admin Console entitas Principal PT ABC
7. Ketik Search `{idFree}`, tekan Enter
8. Verifikasi Activity Log entitas approver (Principal PT ABC) memuat satu entri Action `Approve`, Object `License Allocation`, Name `{idFree}`, Field `Status`, Old `Waiting for Approval`, New `Active`, Modified By `Hendra W`
9. Buka Allocation > License Allocation (tab Current)
10. Klik ikon `Changelog` pada List
11. Verifikasi modal Changelog menampilkan sedikitnya satu baris entri
12. Verifikasi jumlah entri Changelog modul sama dengan `{nChangelog}` (Changelog modul tidak bertambah)
13. Tutup modal Changelog
14. Ganti akun: Logout dari Hendra Wijaya
15. Login sebagai Fajar Nugroho (`totalControlDistLic`, password `Spectra.env.AC_LA_TC_DIST_PASSWORD`), staf Plan Owner PT Maju Bersama
16. Buka Activity Log Admin Console entitas PT Maju Bersama
17. Ketik Search `{idFree}`, tekan Enter
18. Verifikasi Activity Log entitas Plan Owner PT Maju Bersama memuat entri Approve yang sama (Action `Approve`, Name `{idFree}`) tepat satu kali, bukan duplikat

## Notes

- Langkah penghubung (S-03, R-16): langkah 7 dan 17 (Search entri berdasarkan Allocation ID), langkah 5 (tunggu aksi selesai, 8b.8), langkah 9 (kembali ke List), langkah 13 (menutup modal Changelog), langkah 14 sampai 16 (ganti akun).
- Asersi "Changelog modul tidak bertambah" (TC-AC-LA-517 butir c) adalah scope exclusion dengan anchor positif atas surface yang sama (langkah 11, prinsip 13g) dan baseline agregat (S-12); bukan kelas g murni.
- Pembagian TC lintas spec: TC-AC-LA-393, 394, 402, 403, dan 411 (Approve dan Reject oleh Fajar Nugroho) ada di spec 125.
- Temuan untuk QA:
  - TC-AC-LA-517 tidak menyebut cara menemukan entri di Activity Log kedua entitas; spec memakai Search dengan Allocation ID unik.
  - TC-AC-LA-517 menyebut "Activity Log entitas Principal PT ABC" dan "entitas PT Maju Bersama" tanpa menjelaskan cara berpindah antar entitas; spec membuka Activity Log dari akun yang menjadi staf masing-masing entitas (Hendra Wijaya, lalu Fajar Nugroho).
  - TC-AC-LA-517 menyebut Pre-setup #10 sebagai staf Plan Owner dan juga pemilik alokasi `Sari P` (Pre-setup #60) tanpa menyebut akun `Sari P` di ACC; spec memakai Pre-setup #2 hanya sebagai requester seed.
