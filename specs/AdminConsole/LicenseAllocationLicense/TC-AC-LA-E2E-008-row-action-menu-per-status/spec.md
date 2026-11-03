---
id: TC-AC-LA-E2E-008-row-action-menu-per-status
title: "Row Action Menu per Status: Ikon, Urutan, dan Aksi yang Tersedia"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-8
  - TC-AC-LA-9
  - TC-AC-LA-33
coverage:
  web: automated
---

# Row Action Menu per Status: Ikon, Urutan, dan Aksi yang Tersedia

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update (PT Maju Bersama) (Pre-setup #4) `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini kecuali dinyatakan lain; data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca (hanya menu `⋯` yang dibuka, tidak ada aksi yang dijalankan): #41 alokasi `Waiting for Approval`, #46 alokasi `Pending`, #47 alokasi `Active`, #48 alokasi `Canceled`, #50 alokasi `Rejected` (seluruhnya milik `Dewi A`), dan #51 alokasi `Expired` milik `Rian T`. Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed41, seed46, seed47, seed48, seed50, seed51).
- Tabel parameter untuk TC-AC-LA-33 (langkah yang diulang per baris tabel):

| Status | Allocation ID seed | Tab | Aksi menu yang diharapkan |
|---|---|---|---|
| `Waiting for Approval` | `Fixture.license-allocation-license.seed41` | Current | Allocation Log, Edit, Cancel Allocation |
| `Pending` | `Fixture.license-allocation-license.seed46` | Current | Allocation Log, Edit, Cancel Allocation |
| `Active` | `Fixture.license-allocation-license.seed47` | Current | hanya Allocation Log |
| `Expired` | `Fixture.license-allocation-license.seed51` | History | hanya Allocation Log |
| `Rejected` | `Fixture.license-allocation-license.seed50` | History | hanya Allocation Log |
| `Canceled` | `Fixture.license-allocation-license.seed48` | History | Allocation Log dan Resubmit |

- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-8: Row action menu: ikon, severity, dan urutan

1. Ketik Search Allocation ID seed `Waiting for Approval` milik `Dewi A` (`Fixture.license-allocation-license.seed41`), tekan Enter
2. Klik ikon `⋯` pada baris `Waiting for Approval` milik `Dewi A` sendiri
3. Amati opsi menu
4. Verifikasi menu overlay berisi urutan: `Allocation Log` (ikon FileInfoLine, dark), `Edit` (ikon Edit2Line, dark), `Cancel Allocation` (ikon CloseLine, danger)
5. Verifikasi semua aksi severity dark tampil sebelum aksi danger
6. Verifikasi tidak ada opsi `Delete`, `Revoke`, `Approve`, maupun `Reject`

### TC-AC-LA-9: Row action Resubmit memakai ikon RefreshLine dark

7. Klik `(←)` pada kotak Search, lalu klik tab `History`
8. Ketik Search Allocation ID seed `Canceled` milik `Dewi A` (`Fixture.license-allocation-license.seed48`), tekan Enter
9. Klik ikon `⋯` pada baris `Canceled` milik `Dewi A` sendiri
10. Verifikasi menu berisi `Allocation Log` (ikon FileInfoLine, dark) dan `Resubmit` (ikon RefreshLine, dark)
11. Verifikasi tidak ada `Edit` dan `Cancel Allocation`

### TC-AC-LA-33: Row action per status

12. Klik `(←)` pada kotak Search, lalu klik tab `Current`
13. Ganti isi kotak search dengan Allocation ID seed baris tabel Prerequisites, tekan Enter (langkah 13 sampai 15 diulang untuk setiap baris tabel dengan Tab Current)
14. Klik ikon `⋯` pada baris hasil Search
15. Verifikasi menu `⋯` memuat aksi pada kolom `Aksi menu yang diharapkan` baris tabel itu
16. Klik `(←)` pada kotak Search, lalu klik tab `History`
17. Ganti isi kotak search dengan Allocation ID seed baris tabel Prerequisites, tekan Enter (langkah 17 sampai 19 diulang untuk setiap baris tabel dengan Tab History)
18. Klik ikon `⋯` pada baris hasil Search
19. Verifikasi menu `⋯` memuat aksi pada kolom `Aksi menu yang diharapkan` baris tabel itu
20. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah `Amati opsi menu`, dan langkah `(←)` pada kotak Search serta pindah tab.
- Langkah 13 sampai 15 diulang untuk tiga baris tabel Tab Current dan langkah 17 sampai 19 untuk tiga baris tabel Tab History; ekspansi 18 langkah, tiap iterasi satu `Verifikasi` per status sesuai Expected a sampai f TC-AC-LA-33.
- Menu `⋯` dibuka lalu dibiarkan; membuka baris lain menggantikan menu sebelumnya. Seluruh seed hanya dibaca.
- Temuan untuk QA:
  - TC-AC-LA-33 Precondition menyebut seluruh alokasi milik `Dewi A` kecuali alokasi `Expired` (Pre-setup #51) milik `Rian T`, sedangkan Pre-setup #51 mendeskripsikannya milik requester `Rian T` (Partner); konsisten dengan TC, dicatat karena akun `Dewi A` hanya memiliki aksi `Allocation Log` pada baris itu.
  - TC-AC-LA-8 dan TC-AC-LA-9 tidak menyebut Allocation ID baris; spec memakai Allocation ID seed Pre-setup #41 dan #48.
