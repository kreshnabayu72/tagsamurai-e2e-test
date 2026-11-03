---
id: TC-GS-NLU-E2E-134-list-filter-chip-opsi-dan-tutup-tanpa-apply
title: "List Filter: chip opsi dihapus lewat tombol silang dan checkbox, serta menutup Filter Panel tanpa Apply"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-273
  - TC-GS-NLU-494
  - TC-GS-NLU-274
coverage:
  web: automated
---

# List Filter: chip opsi dihapus lewat tombol silang dan checkbox, serta menutup Filter Panel tanpa Apply

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): Position yang dipakai baris tabel `Field Technician`, `Driver`, `Contractor`; Non-Login User `Agus Salim` (Contractor) dan `Rina Marlina` (Driver). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengamatan chip di dalam field filter dan titik indikator pada ikon Filter.
- State global: tidak ada yang diubah. State Filter dibersihkan oleh langkah penghubung dan langkah terakhir. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-273: Chip opsi terpilih dihapus lewat tombol silang dan meng-uncheck checkbox opsi terkait

1. Buka Filter Panel, pilih Position `Driver` dan `Contractor`
2. Klik `(✕)` pada chip `Driver`
3. Verifikasi chip `Driver` hilang
4. Verifikasi chip `Contractor` tetap
5. Buka dropdown Position
6. Verifikasi checkbox `Driver` ter-uncheck di dalam dropdown
7. Verifikasi checkbox `Contractor` tetap tercentang
8. Verifikasi tabel belum berubah sebelum `[Apply]`: sedikitnya satu baris dengan Position bukan `Contractor` masih tampil
9. Klik `[Apply]`
10. Verifikasi tabel hanya memuat baris Position `Contractor`: baris `Agus Salim` tampil dan seluruh baris hasil ber-Position `Contractor`

### TC-GS-NLU-494: Chip opsi terpilih hilang saat checkbox opsi di-uncheck dari dalam dropdown

11. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`
12. Buka Filter Panel, pilih Position `Driver` dan `Contractor`
13. Buka dropdown Position dan hapus centang `Contractor`
14. Verifikasi chip `Contractor` hilang dari field Position
15. Verifikasi chip `Driver` tetap
16. Verifikasi tabel belum berubah sebelum `[Apply]`: sedikitnya satu baris dengan Position bukan `Driver` masih tampil
17. Klik `[Apply]`
18. Verifikasi tabel hanya memuat baris Position `Driver`: baris `Rina Marlina` tampil dan seluruh baris hasil ber-Position `Driver`

### TC-GS-NLU-274: Menutup Filter Panel tanpa Apply membuang perubahan dan indikator titik muncul saat filter aktif

19. Buka Filter Panel, klik `[Clear Field]`, pilih Position `Driver`, klik `[Apply]`
20. Verifikasi ikon Filter menampilkan titik indikator
21. Buka Filter Panel, ubah Position menjadi `Contractor` tanpa Apply (hapus centang `Driver`, centang `Contractor`), klik ikon Filter untuk menutup
22. Buka lagi Filter Panel
23. Verifikasi panel menampilkan nilai ter-Apply terakhir (`Driver`), bukan draf `Contractor`
24. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): `[Clear Field]` lalu `[Apply]` yang membersihkan Filter sebelum TC berikutnya (S-09) dan pada langkah terakhir; membuka Filter Panel di awal tiap TC. Asumsi dari TC-GS-NLU-274 dan TC-GS-NLU-275: `[Apply]` menutup Filter Panel, sehingga setiap TC membuka panel lagi.
- Asersi tambahan (S-03): baris `Agus Salim` dan `Rina Marlina` menjadi anchor asersi universal "hanya baris Position ..." (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-GS-NLU-267, TC-GS-NLU-268, dan TC-GS-NLU-272 ada di spec 078.
- Temuan untuk QA:
  - TC-GS-NLU-273 dan TC-GS-NLU-494 tidak menyebut baris pembanding untuk "tabel belum berubah"; spec memakai baris Position bukan `Contractor` atau bukan `Driver`.
  - TC-GS-NLU-274 Expected a menyebut indikator titik "selama ada filter ter-Apply"; TC tidak memberi langkah observasi saat filter tidak aktif, sehingga hanya keadaan aktif yang diasersi.
