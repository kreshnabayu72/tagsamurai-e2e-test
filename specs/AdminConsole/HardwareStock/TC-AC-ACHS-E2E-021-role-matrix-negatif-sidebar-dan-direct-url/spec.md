---
id: TC-AC-ACHS-E2E-021-role-matrix-negatif-sidebar-dan-direct-url
title: "Role Matrix Negatif: Menu Sidebar Hidden dan Direct URL Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-58
  - TC-AC-ACHS-59
  - TC-AC-ACHS-60
  - TC-AC-ACHS-61
  - TC-AC-ACHS-62
  - TC-AC-ACHS-63
  - TC-AC-ACHS-75
  - TC-AC-ACHS-201
coverage:
  web: automated
---

# Role Matrix Negatif: Menu Sidebar Hidden dan Direct URL Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun default suite: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Semua akun yang diuji di bawah memakai Step ganti akun eksplisit (logout lalu login); hook `after` mengembalikan sesi ke akun default suite. Password akun selain Total Control memakai nama env `AC_<ROLE>_PASSWORD` yang ditetapkan tim FE (belum terdaftar; lihat Temuan untuk QA).
- Tabel "Role sidebar" (parameter langkah 2 sampai 6):

  | Role | Akun (Pre-setup) | TC |
  |---|---|---|
  | Role lain tanpa capability Manage hardware stock | `{Fixture.hardwareStock.account.p08.noCapability.email}` (No 8) | 58 |
  | Group Manager tanpa assignment Global Role Manage hardware stock | `{Fixture.hardwareStock.account.p09.groupManager.email}` (No 9) | 59 |
  | Distributor Pre-setup No 13 tanpa role Manage hardware stock | `{Fixture.hardwareStock.account.p13.distributorNoRole.email}` (No 13) | 60 |
  | Partner Pre-setup No 14, 0-access | `{Fixture.hardwareStock.account.p14.partner.email}` (No 14) | 61 |

- Tabel "Role direct URL Stock List" (parameter langkah 7 sampai 13):

  | Role | Akun (Pre-setup) | TC |
  |---|---|---|
  | Partner Pre-setup No 14 | `{Fixture.hardwareStock.account.p14.partner.email}` (No 14) | 62 |
  | Role lain tanpa capability Manage hardware stock | `{Fixture.hardwareStock.account.p08.noCapability.email}` (No 8) | 63 |

- Akun blok lain: Distributor, Local Registration aktif, `{Fixture.hardwareStock.account.p10.distributorCakra.email}` (No 10; TC-75); Create-Only `{Fixture.hardwareStock.account.p04.createOnly.email}` (No 4; TC-201).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.account.p08.noCapability.email}` | No 8 | email akun Pre-setup No 8 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p08.noCapability.email` |
  | `{Fixture.hardwareStock.account.p09.groupManager.email}` | No 9 | email akun Pre-setup No 9 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p09.groupManager.email` |
  | `{Fixture.hardwareStock.account.p13.distributorNoRole.email}` | No 13 | email akun Pre-setup No 13 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p13.distributorNoRole.email` |
  | `{Fixture.hardwareStock.account.p14.partner.email}` | No 14 | email akun Pre-setup No 14 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p14.partner.email` |
  | `{Fixture.hardwareStock.account.p10.distributorCakra.email}` | No 10 | email akun Pre-setup No 10 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p10.distributorCakra.email` |
  | `{Fixture.hardwareStock.account.p04.createOnly.email}` | No 4 | email akun Pre-setup No 4 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p04.createOnly.email` |

- Kemampuan teknis (disediakan tim FE): URL halaman Hardware > Stock dan URL halaman Approvals > Hardware Stock disediakan sebagai konstanta fixture (URL tidak tertulis di TC); mengetik URL langsung di address bar.
- Data Pre-setup (hanya dibaca): akun di atas dan Katalog SKU (No 16). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen untuk akun aktor default suite (lihat suite.md). Flag untuk akun pada tabel dan blok di atas tidak relevan karena akun tersebut tidak membuka halaman modul.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Menu sidebar Hidden (TC-AC-ACHS-58, 59, 60, 61)

1. Untuk setiap baris tabel "Role sidebar" pada Prerequisites, lakukan langkah 2 sampai 6
2. Logout, lalu login sebagai akun pada baris tabel
3. Verifikasi sidebar Admin Console tampil dengan sedikitnya satu item menu
4. Telusuri seluruh grup menu sidebar dan cari entri `Hardware > Stock`
5. Verifikasi menu `Hardware > Stock` tidak muncul di sidebar
6. Verifikasi menu `Approvals > Hardware Stock` tidak muncul di sidebar untuk aktor ini

### Direct URL Stock List ditolak (TC-AC-ACHS-62, 63)

7. Untuk setiap baris tabel "Role direct URL Stock List" pada Prerequisites, lakukan langkah 8 sampai 13
8. Logout, lalu login sebagai akun pada baris tabel
9. Ketik URL halaman Hardware > Stock langsung di address bar, tekan Enter
10. Verifikasi muncul toast error "You don't have permission to do this."
11. Verifikasi UI di-refresh tanpa elemen modul (Breadcrumb `Hardware > Stock` dan Table Tools Stock List tidak tampil)
12. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
13. Verifikasi tidak ada data Stock List yang tampil

### Distributor tidak dapat membuka Approvals lewat URL (TC-AC-ACHS-75)

14. Logout, lalu login sebagai Distributor (Pre-setup No 10)
15. Ketik URL halaman Approvals > Hardware Stock langsung di address bar, tekan Enter
16. Verifikasi muncul toast error "You don't have permission to do this."
17. Verifikasi UI di-refresh tanpa redirect
18. Verifikasi tidak ada data approval yang tampil

### Aktor tanpa tier approver tidak memiliki akses Approvals (TC-AC-ACHS-201)

19. Logout, lalu login sebagai Create-Only (Pre-setup No 4)
20. Verifikasi menu `Hardware > Stock` tampil di sidebar
21. Verifikasi menu `Approvals > Hardware Stock` tidak muncul di sidebar
22. Ketik URL halaman Approvals > Hardware Stock langsung di address bar, tekan Enter
23. Verifikasi akses URL ditolak dengan toast error "You don't have permission to do this."
24. Verifikasi akses URL ditolak tanpa redirect

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-58, 59, 60, 61, 62, 63, 75, 201). Tidak ada TC hanya-BE di spec ini.
- Spec Role Matrix negatif varian A. TC-58 sampai TC-61 (langkah identik, hanya akun berbeda) dan TC-62 dengan TC-63 (langkah identik) ditulis sebagai perulangan "Untuk setiap baris tabel" (langkah 2 sampai 6 dan 8 sampai 13); id TC tetap lengkap di `sourceTc`. TC-75 dan TC-201 ditulis per blok karena langkahnya berbeda.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): Step ganti akun pada tiap blok (logout lalu login; akun default suite login di hook `before`, sehingga tiap blok memerlukan ganti akun eksplisit). Verifikasi sidebar tampil dan menu `Hardware > Stock` tampil (TC-201) adalah anchor positif untuk asersi absence menu (bagian 8b butir 2); Expected TC tidak memuatnya.
- Langkah 2 sampai 6 diulang empat kali dan langkah 8 sampai 13 diulang dua kali; ekspansi menghasilkan langkah di atas smell 35 langkah. Alasan: semua blok adalah Role Matrix negatif satu kelas yang berdiri sendiri tanpa data bersama; kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah 4: TC berbunyi "Buka sidebar dan telusuri seluruh grup menu" lalu "cari entri"; keduanya digabung dalam satu langkah aksi.
- Temuan untuk QA:
  - TC-62 dan TC-63 Expected b ("UI di-refresh tanpa elemen modul") tidak mendefinisikan elemen yang diasersi; spec mengasersi Breadcrumb `Hardware > Stock` dan Table Tools Stock List tidak tampil. Expected c ("tidak ada redirect ke halaman unauthorized terpisah") diasersi dengan URL halaman yang tidak berubah menjadi halaman lain.
  - TC-62, 63, 75, dan 201 tidak menyebut URL halaman yang diketik; URL disediakan sebagai konstanta fixture oleh tim FE.
  - TC-201 judul menyebut "Create-only dan Delete-only", tetapi Precondition, Langkah Uji, dan Expected hanya memuat aktor Create-Only; spec hanya menguji Create-Only. Aktor Delete-Only (Pre-setup No 5) tidak memiliki TC sumber untuk kombinasi ini; diusulkan sebagai TC baru bila diperlukan.
  - TC-75 Expected b ("UI di-refresh tanpa redirect") sama ambigunya dengan TC-62 Expected b; spec mengasersi tidak ada redirect dan tidak ada data approval.
  - Tidak ada literal Pre-setup; email akun aktor dirujuk lewat kunci `account.*` pada tabel Parameter Pre-setup: nama orang dan company diganti rujukan nomor Pre-setup sehingga tidak memerlukan pengecualian S-12.
  - Password akun selain Total Control memakai nama env `AC_<ROLE>_PASSWORD` yang belum terdaftar; diminta dari tim FE.
