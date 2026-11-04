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
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE). Semua permintaan pada data ini ditolak sehingga tidak ada yang berubah:
  - Akun terekspor: Code `DID071A`, Account Name `Akun Terekspor {runId}-071`, Function Capitalization Offset, Active, Used By 0, Last Used in Journal terisi (diekspor hook `before` lewat jalur Journal J-06 yang disediakan tim FE/BE); padanan P2 pada TC-FA-COA-36, 110, dan 111.
  - Akun dipakai Asset Class: Code `DID071B`, Account Name `Akun Dipakai {runId}-071`, Function Depreciation Expense, Active, Used By 1 oleh Asset Class `Asset Class Pemakai {runId}-071` yang dibuat hook `before` dan dihapus hook `after`; belum pernah diekspor; padanan P6 pada TC-FA-COA-124.
  - Akun milik client B (client lain di luar client A): Code `DID071C`, Account Name `Akun Client B {runId}-071`, di-seed hook `before` pada client B; identitas client B tidak tertulis di TC dan disediakan tim FE (lihat Temuan untuk QA). Dipakai TC-FA-COA-109.
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID071A`, `DID071B`, `DID071C`, dan `DID071X` (Code tujuan perubahan yang selalu ditolak) memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (ubah Account Code, ubah Account Function, Delete, baca akun menurut ID) dengan sesi API aktor Total Control client A; pembacaan akun dari server beserta Code, Function, dan keberadaannya.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Seed dan pemulihan serta fixture Asset Class mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-36: Ubah Account Code akun pernah diekspor

1. Kirim permintaan ubah Account Code `DID071A` menjadi `DID071X` langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
2. Verifikasi permintaan ditolak server
3. Verifikasi akun `DID071A` tetap `DID071A` pada data dari server

### TC-FA-COA-109: Akun client lain tidak dapat dibaca atau diubah lewat ID

4. Kirim permintaan baca akun `DID071C` milik client B menurut ID langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
5. Verifikasi data akun client B tidak dikembalikan pada respons
6. Kirim permintaan ubah akun `DID071C` milik client B menurut ID langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
7. Verifikasi perubahan ditolak server

### TC-FA-COA-110: Ubah Account Function akun terkunci

8. Kirim permintaan ubah Account Function `DID071A` menjadi Gain on Disposal langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
9. Verifikasi respons ditolak server
10. Verifikasi Function `DID071A` tetap Capitalization Offset pada data dari server

### TC-FA-COA-111: Delete akun terekspor

11. Kirim permintaan Delete `DID071A` langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
12. Verifikasi respons ditolak server
13. Verifikasi akun `DID071A` tetap ada pada data dari server

### TC-FA-COA-124: Ubah Account Function akun yang dipakai Asset Class

14. Kirim permintaan ubah Account Function `DID071B` menjadi Asset Cost langsung ke server menggunakan sesi API aktor Total Control client A hingga respons diterima
15. Verifikasi permintaan ditolak server
16. Verifikasi Function `DID071B` tetap Depreciation Expense pada data dari server

## Notes

- `K-1`: TC-FA-COA-36, 109, 110, 111, dan 124 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan kontrak API, karena TC granular tetap sumber.
- Pembagian TC lintas spec (S-05): klausa "tidak ada log" pada Expected b TC-FA-COA-36 dan TC-FA-COA-124 diasersi di spec 096, yang memuat permintaan langsung yang sama dengan baseline sendiri. Spec ini hanya mengasersi respons server dan state data.
- Target aksi memakai akun milik spec (S-06): TC memakai P2 dan P6, spec memakai `DID071A` dan `DID071B` dengan state yang sama; akun client B juga milik spec.
- Langkah 4 dan 6 memecah satu langkah TC ("baca dan ubah") menjadi dua permintaan agar tiap Expected (data tidak dikembalikan, perubahan ditolak) punya langkah Verifikasi sendiri tepat setelah aksinya (R-03).
- Tanpa langkah UI; "Login sbg Role: Total Control" dipenuhi hook `before` dan sesi API aktor.
- Temuan untuk QA:
  - TC-FA-COA-36, 109, 110, 111, dan 124 menyebut "ditolak server" tanpa kode status; spec tidak mengasersi kode tertentu.
  - TC-FA-COA-109 tidak menyebut client B, akun yang dipakai, atau ID akunnya (kolom ACC hanya "Akun milik client B ada"); identitas client B disediakan tim FE dan akun `DID071C` di-seed hook `before` pada client B.
  - TC-FA-COA-36 menyebut Code tujuan `6-2002`; spec memakai `DID071X` karena akun asal adalah akun milik spec.
  - TC-FA-COA-109 tidak memberi cara memeriksa bahwa data client B tidak berubah sesudah permintaan ubah ditolak; hanya penolakan yang diasersi.
