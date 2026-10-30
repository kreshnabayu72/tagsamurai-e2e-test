---
id: TC-GS-ROLE-E2E-007-no-result-search-pada-tab-total-control-read-only-system-dan-detail
title: "No-Result Search pada Tab Total Control, Tab Read Only, Tab System, dan Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-19
coverage:
  web: automated
---

# No-Result Search pada Tab Total Control, Tab Read Only, Tab System, dan Detail

## Prerequisites

- Mode: FE+BE.
- Aktor: Ahmad Fauzi (Total Control, Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Role & Permission dengan Tab Total Control aktif.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup: Tab Total Control, Tab Read Only (Pre-setup #4), Tab System, dan Detail "Manage TAG" berisi data sehingga Search `zzqx` tidak cocok dengan baris mana pun.
- Spec hanya membaca data; tidak ada data yang dibuat, diubah, atau dihapus, sehingga tidak ada pemulihan Pre-setup.
- Data uji: Keyword `zzqx`.

## Test Steps

### TC-GS-ROLE-19: No-result state pada Tab Total Control, Read Only, System, dan Detail

1. Ketik Search `zzqx`, tekan Enter
2. Verifikasi Tab Total Control menampilkan Illustration
3. Verifikasi Tab Total Control menampilkan Title "No results found"
4. Verifikasi Tab Total Control menampilkan Description "Try adjusting your search or filter."
5. Klik `(←)` pada kotak Search
6. Klik Tab Read Only
7. Ketik Search `zzqx`, tekan Enter
8. Verifikasi Tab Read Only menampilkan Illustration
9. Verifikasi Tab Read Only menampilkan Title "No results found"
10. Verifikasi Tab Read Only menampilkan Description "Try adjusting your search or filter."
11. Klik `(←)` pada kotak Search
12. Klik Tab System
13. Ketik Search `zzqx`, tekan Enter
14. Verifikasi Tab System menampilkan Illustration
15. Verifikasi Tab System menampilkan Title "No results found"
16. Verifikasi Tab System menampilkan Description "Try adjusting your search or filter."
17. Klik `(←)` pada kotak Search
18. Klik Role Name `Manage TAG`
19. Ketik Search `zzqx`, tekan Enter
20. Verifikasi Detail menampilkan Illustration
21. Verifikasi Detail menampilkan Title "No results found"
22. Verifikasi Detail menampilkan Description "Try adjusting your search or filter."

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular (spec memuat satu TC).
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): mengosongkan kotak Search sebelum berpindah surface (langkah 5, 11, 17) dan berpindah tab atau membuka Detail (langkah 6, 12, 18). Pengosongan pada langkah 17 diperlukan karena baris `Manage TAG` tidak tampil selama Search `zzqx` aktif di Tab System.
- Expected "Illustration + Title + Description" dipecah menjadi tiga `Verifikasi` per surface (S-01). "idem" pada butir b, c, dan d diasersi dengan teks yang sama dengan butir a.
- Temuan untuk QA:
  - TC-GS-ROLE-19 langkah 2 sampai 4 ("Ulangi") tidak menyebut apakah kotak Search tetap berisi `zzqx` setelah berpindah tab; spec mengosongkan Search sebelum berpindah dan mengetik ulang di tiap surface.
  - TC-GS-ROLE-19 langkah 4 tidak menyebut Detail role yang dipakai pada Data Uji; langkah memakai Detail "Manage TAG" (sesuai langkah TC).
