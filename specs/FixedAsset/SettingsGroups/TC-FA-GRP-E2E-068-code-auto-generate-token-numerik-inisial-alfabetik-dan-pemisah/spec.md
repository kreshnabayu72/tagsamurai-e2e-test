---
id: TC-FA-GRP-E2E-068-code-auto-generate-token-numerik-inisial-alfabetik-dan-pemisah
title: "Code Auto-Generate: Token Numerik Passthrough, Inisial per Token Alfabetik, dan Pemisah -, _, /"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-321
  - TC-FA-GRP-322
  - TC-FA-GRP-323
coverage:
  web: automated
---

# Code Auto-Generate: Token Numerik Passthrough, Inisial per Token Alfabetik, dan Pemisah -, _, /

## Prerequisites

- Mode: FE+BE (backend nyata; Code auto-generate dihitung server saat Create dan dibaca di tabel).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data uji (iterasi langkah 1 sampai 7): tabel "Name dan Code hasil" berikut; Name literal (tanpa suffix) karena Code auto-generate diturunkan dari token Name (lihat Temuan untuk QA); kandidat Code belum dipakai (precondition TC-FA-GRP-321, 322, 323).

| Name (Code dikosongkan) | Code hasil | TC |
|---|---|---|
| `Room 301` | `R301` | TC-FA-GRP-321 |
| `Head Office Annex` | `HOA` | TC-FA-GRP-322 |
| `north-west_wing/b` | `NWWB` | TC-FA-GRP-323 |

- Kemampuan teknis: tidak ada selain pembacaan kolom Code di tabel Groups List.
- Pemulihan (hook `before` dan `after`): hapus lewat API group literal `Room 301`, `Head Office Annex`, `north-west_wing/b`, dan group ber-Code `R301`, `HOA`, `NWWB` (hook `before` juga menghapus sisa literal run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-321 sampai TC-FA-GRP-323: Code auto-generate (token numerik, inisial alfabetik, pemisah)

1. Untuk setiap baris tabel "Name dan Code hasil" pada Prerequisites (langkah 1 sampai 7): klik [+] Group di sidebar, lalu isi Group Name dengan Name baris itu dan biarkan Code kosong
2. Verifikasi Code tetap kosong dan tidak ada live preview Code di popup sebelum submit
3. Klik [Submit]
4. Verifikasi toast sukses `Success, group has been created.`
5. Ketik Search Name baris itu, tekan Enter
6. Verifikasi Code tersimpan sesuai kolom Code hasil baris itu
7. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular; ketiga TC memakai langkah identik sehingga ditulis sebagai satu perulangan atas tabel Prerequisites (8b butir 7).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 5 (Ketik Search Name baris itu, tekan Enter); langkah 7 (Klik `(←)` pada kotak Search).
- Langkah 1 sampai 7 berulang untuk tiga baris tabel (ekspansi 3 x 7 = 21 langkah); `Verifikasi` tetap satu per klausa (S-01). Asersi "tidak ada live preview Code" diletakkan sebelum [Submit] dan memakai kolom Code yang tetap kosong sebagai bukti.
- Temuan untuk QA:
  - Name Code auto-generate harus literal (`Room 301`, `Head Office Annex`, `north-west_wing/b`) karena token Name menentukan Code (`R301`, `HOA`, `NWWB`); suffix per run mengubah hasil. Butuh butir Lampiran A modul Groups (S-12).
  - TC-FA-GRP-321, 322, dan 323 tidak menyebut parent; group dibuat di level 1 lewat [+] Group.
  - TC-FA-GRP-321 Expected c "Tidak ada live preview Code di popup sebelum submit" tidak menyebut cara membuktikannya; spec mengasersi field Code tetap kosong sebelum [Submit].

