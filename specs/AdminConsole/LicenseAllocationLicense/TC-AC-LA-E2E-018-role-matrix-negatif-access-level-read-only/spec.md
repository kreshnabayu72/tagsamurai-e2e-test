---
id: TC-AC-LA-E2E-018-role-matrix-negatif-access-level-read-only
title: "Role Matrix Negatif: Access Level Read Only Tidak Dapat Mengubah"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-70
  - TC-AC-LA-71
coverage:
  web: automated
---

# Role Matrix Negatif: Access Level Read Only Tidak Dapat Mengubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Read Only Principal (Pre-setup #3) `readOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rina Wijaya`), password `Spectra.env.AC_LA_READ_ONLY_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Read Only Distributor (Pre-setup #14) `readOnlyDistLic_automated_{namaCompany}@qwertysystem.net` (`Lina Marlina`), password `Spectra.env.AC_LA_READ_ONLY_DIST_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Hasil yang diuji |
|---|---|---|
| `readOnlyLic` (`Rina Wijaya`) | Read Only Principal | `[+ Allocation]`, `Edit`, `Cancel Allocation`, `Resubmit` Hidden; `Allocation Log`, Download, Changelog Show; Approve dan Reject tidak tersedia |
| `readOnlyDistLic` (`Lina Marlina`) | Read Only Distributor | data dalam jaringan tampil; `[+ Allocation]`, `Edit`, `Cancel Allocation`, `Resubmit` Hidden |

- Data Pre-setup yang dibaca: #41 alokasi `Waiting for Approval` dan #48 alokasi `Canceled`; Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seed41, seed48). Seed hanya dibaca.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### Akun `readOnlyLic` (TC-AC-LA-70)

1. Ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
2. Verifikasi ikon Download dan ikon Changelog Show
3. Verifikasi `[+ Allocation]` Hidden pada toolbar tab Current
4. Klik ikon `⋯` pada baris `Waiting for Approval`
5. Verifikasi row action `Allocation Log` Show
6. Verifikasi row action `Edit` dan `Cancel Allocation` Hidden
7. Verifikasi opsi Approve dan Reject tidak tersedia pada menu `⋯`
8. Klik `Allocation Log`
9. Verifikasi modal `Allocation Log` terbuka
10. Tutup modal dengan `[×]`, lalu klik `(←)` pada kotak Search
11. Klik tab `History`, lalu ketik Search Allocation ID seed `Canceled` (`Fixture.license-allocation-license.seed48`), tekan Enter
12. Klik ikon `⋯` pada baris `Canceled`
13. Verifikasi row action `Allocation Log` Show
14. Verifikasi row action `Resubmit` Hidden

### Akun `readOnlyDistLic` (TC-AC-LA-71)

15. Ganti akun: Logout lalu login sebagai Read Only Distributor (`readOnlyDistLic`), lalu buka Allocation > License Allocation tab Current
16. Verifikasi sedikitnya satu baris data dalam jaringan Distributor tampil pada tab Current
17. Verifikasi `[+ Allocation]` Hidden pada toolbar tab Current
18. Ketik Search Allocation ID seed `Waiting for Approval` (`Fixture.license-allocation-license.seed41`), tekan Enter
19. Klik ikon `⋯` pada baris `Waiting for Approval`
20. Verifikasi row action `Allocation Log` Show
21. Verifikasi row action `Edit` dan `Cancel Allocation` Hidden
22. Klik `(←)` pada kotak Search, lalu klik tab `History`, lalu ketik Search Allocation ID seed `Canceled` (`Fixture.license-allocation-license.seed48`), tekan Enter
23. Klik ikon `⋯` pada baris `Canceled`
24. Verifikasi row action `Allocation Log` Show pada menu `⋯` baris `Canceled` (anchor menu terbuka)
25. Verifikasi row action `Resubmit` Hidden

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah membuka menu `⋯`, penutupan modal, dan ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): pembukaan Allocation > License Allocation tab Current di dalam langkah Ganti akun, karena halaman landing akun tidak diandaikan (S-07).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil berbeda per role.
- Asersi tambahan (S-03): langkah 24 (`Allocation Log` Show) adalah anchor positif sebelum asersi `Resubmit` Hidden bagi `readOnlyDistLic`, selaras dengan anchor langkah 20 dan 13; alasannya bagian 8b butir 2 dan keputusan 2026-11-04.
- Spec negatif: aksi tulis tidak tersedia bagi access level Read Only; anchor absence berupa row action `Allocation Log` yang tampil pada menu `⋯` yang sama (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-71 Expected a (`Data dalam jaringan Distributor tampil`) tidak merinci data; spec mengasersi sedikitnya satu baris tampil.
  - TC-AC-LA-70 dan TC-AC-LA-71 tidak mengasersi penolakan server atas request langsung bagi access level Read Only; hanya visibilitas UI yang diuji.
