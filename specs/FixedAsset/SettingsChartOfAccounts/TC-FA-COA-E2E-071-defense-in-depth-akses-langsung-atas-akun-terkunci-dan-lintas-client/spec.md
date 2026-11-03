---
id: TC-FA-COA-E2E-071-defense-in-depth-akses-langsung-atas-akun-terkunci-dan-lintas-client
title: "Defense-in-Depth: Akses Langsung atas Akun Terkunci dan Lintas Client"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-36
  - TC-FA-COA-109
  - TC-FA-COA-110
  - TC-FA-COA-111
  - TC-FA-COA-124
coverage:
  web: automated
---

# Defense-in-Depth: Akses Langsung atas Akun Terkunci dan Lintas Client

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI). Spec hanya mengasersi respons server dan state data (bagian 8b butir 1, `K-1`); asersi absence log tidak ada di spec ini (lihat Notes).
- Akun aktor: Total Control client A `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Semua permintaan langsung memakai sesi API aktor Total Control client A (butir "Sesi API aktor" di `suite.md`); tidak ada ganti akun UI.
- Data Pre-setup yang hanya menjadi target permintaan yang ditolak, tidak diubah (S-06; efek pada Last Updated: tidak ada karena semua permintaan ditolak):
  - P2 `6-2001 - Repairs & Maintenance Expense`: Function Capitalization Offset, Active, Used By 0, pernah diekspor (Last Used in Journal `Aug 2026`). Dipakai TC-FA-COA-36, 110, dan 111; keadaan "pernah diekspor" tidak dapat dibuat oleh spec.
  - P6 `5-6002 - Depreciation Expense - Warehouse`: Function Depreciation Expense, Active, Used By 1 (Asset Class `Office Equipment`), belum pernah diekspor. Dipakai TC-FA-COA-124; fixture Asset Class pemakai disediakan tim FE.
  - Akun milik client B (client lain di luar client A): identitas client dan ID akun tidak tertulis di TC; disediakan tim FE (lihat Temuan untuk QA). Dipakai TC-FA-COA-109.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (ubah Account Code, ubah Account Function, Delete, baca akun menurut ID) dengan sesi API aktor Total Control client A; pembacaan akun dari server beserta Code, Function, dan keberadaannya.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Seed dan pemulihan Pre-setup serta fixture Asset Class mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; jalur ekspor Journal J-06 untuk keadaan P2 "pernah diekspor" disediakan tim FE/BE. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-36: Ubah Account Code akun pernah diekspor

1. Kirim permintaan ubah Account Code P2 `6-2001` menjadi `6-2002` langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
2. Verifikasi permintaan ditolak server
3. Verifikasi akun P2 tetap `6-2001` pada data dari server

### TC-FA-COA-109: Akun client lain tidak dapat dibaca atau diubah lewat ID

4. Kirim permintaan baca akun milik client B menurut ID langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
5. Verifikasi data akun client B tidak dikembalikan pada respons
6. Kirim permintaan ubah akun milik client B menurut ID langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
7. Verifikasi perubahan ditolak server

### TC-FA-COA-110: Ubah Account Function akun terkunci

8. Kirim permintaan ubah Account Function P2 menjadi Gain on Disposal langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
9. Verifikasi respons ditolak server
10. Verifikasi Function P2 tetap Capitalization Offset pada data dari server

### TC-FA-COA-111: Delete akun terekspor

11. Kirim permintaan Delete P2 langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
12. Verifikasi respons ditolak server
13. Verifikasi akun P2 tetap ada pada data dari server

### TC-FA-COA-124: Ubah Account Function akun yang dipakai Asset Class

14. Kirim permintaan ubah Account Function P6 menjadi Asset Cost langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
15. Verifikasi permintaan ditolak server
16. Verifikasi Function P6 tetap Depreciation Expense pada data dari server

## Notes

- `K-1`: TC-FA-COA-36, 109, 110, 111, dan 124 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan kontrak API, karena TC granular tetap sumber.
- Klausa "tidak ada log" pada Expected TC-FA-COA-36 b dan TC-FA-COA-124 b tidak diasersi di spec ini (S-05); belum ada spec absence yang memuatnya (lihat Temuan untuk QA).
- Langkah 4 dan 6 memecah satu langkah TC ("baca dan ubah") menjadi dua permintaan agar tiap Expected (data tidak dikembalikan, perubahan ditolak) punya langkah Verifikasi sendiri tepat setelah aksinya (R-03).
- Tanpa langkah UI; "Login sbg Role: Total Control" dipenuhi hook `before` dan sesi API aktor.
- Temuan untuk QA:
  - TC-FA-COA-36, 109, 110, 111, dan 124 menyebut "ditolak server" tanpa kode status; spec tidak mengasersi kode tertentu.
  - TC-FA-COA-109 tidak menyebut client B, akun yang dipakai, atau ID akunnya (kolom ACC hanya "Akun milik client B ada"); identitas disediakan tim FE.
  - TC-FA-COA-36 dan 124 Expected b memuat klausa "tidak ada log" yang tidak dimiliki spec absence mana pun; belum diasersi.
  - TC-FA-COA-109 tidak memberi cara memeriksa bahwa data client B tidak berubah sesudah permintaan ubah ditolak; hanya penolakan yang diasersi.
