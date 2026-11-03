---
id: TC-FA-GRP-E2E-069-code-auto-generate-token-alfanumerik-karakter-tidak-valid-dan-fallback-empat-karakter-acak
title: "Code Auto-Generate: Token Alfanumerik, Karakter Tidak Valid, Token Tanpa Karakter Valid, dan Fallback 4 Karakter Acak"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-324
  - TC-FA-GRP-325
  - TC-FA-GRP-326
  - TC-FA-GRP-327
  - TC-FA-GRP-328
coverage:
  web: automated
---

# Code Auto-Generate: Token Alfanumerik, Karakter Tidak Valid, Token Tanpa Karakter Valid, dan Fallback 4 Karakter Acak

## Prerequisites

- Mode: FE+BE (backend nyata; Code auto-generate dihitung server saat Create dan dibaca di tabel).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data uji (iterasi blok pertama langkah 1 sampai 7): tabel "Name dan Code hasil" berikut; Name literal (tanpa suffix) karena Code auto-generate diturunkan dari token Name (lihat Temuan untuk QA); kandidat Code belum dipakai (precondition TC-FA-GRP-324 dan 325); pada TC-FA-GRP-326 kandidat Code `SR` sudah dipakai Server Room (Pre-setup No 9) dan `SR2` belum dipakai, sehingga dedup Tier 1 memakai suffix angka (token `***` dilewati).

| Name (Code dikosongkan) | Code hasil | TC |
|---|---|---|
| `Lab 2F` | `L2` | TC-FA-GRP-324 |
| `#Lab @Main` | `LM` | TC-FA-GRP-325 |
| `*** Store Room` | `SR2` | TC-FA-GRP-326 |

- Data uji blok fallback acak (iterasi langkah 8 sampai 11): tabel "Name fallback" berikut; hasil Code = 4 karakter acak huruf besar A-Z atau angka 0-9.

| Name (Code dikosongkan) | Alasan fallback | TC |
|---|---|---|
| `Annex` | kandidat `A` kurang dari 2 karakter | TC-FA-GRP-327 |
| `*** ###` | nama tanpa karakter valid | TC-FA-GRP-328 |

- Kemampuan teknis: tidak ada selain pembacaan kolom Code di tabel Groups List.
- Pemulihan (hook `before` dan `after`): hapus lewat API group literal `Lab 2F`, `#Lab @Main`, `*** Store Room`, `Annex`, `*** ###`, dan group ber-Code `L2`, `LM`, `SR2` yang dibuat spec ini (hook `before` juga menghapus sisa literal run sebelumnya). Group `Server Room` Pre-setup (Code `SR`) tidak diubah.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-324 sampai TC-FA-GRP-326: Code auto-generate (alfanumerik, karakter tidak valid, token tanpa karakter valid)

1. Untuk setiap baris tabel "Name dan Code hasil" pada Prerequisites (langkah 1 sampai 7): klik [+] Group di sidebar, lalu isi Group Name dengan Name baris itu dan biarkan Code kosong
2. Verifikasi Code tetap kosong dan tidak ada live preview Code di popup sebelum submit
3. Klik [Submit]
4. Verifikasi toast sukses `Success, group has been created.`
5. Ketik Search Name baris itu, tekan Enter
6. Verifikasi Code tersimpan sesuai kolom Code hasil baris itu
7. Klik `(←)` pada kotak Search

### TC-FA-GRP-327 dan TC-FA-GRP-328: Fallback 4 karakter acak

8. Untuk setiap baris tabel "Name fallback" pada Prerequisites (langkah 8 sampai 11): klik [+] Group di sidebar, isi Group Name dengan Name baris itu dan biarkan Code kosong, lalu klik [Submit]
9. Ketik Search Name baris itu, tekan Enter
10. Verifikasi Code tersimpan 4 karakter acak huruf besar A-Z atau angka 0-9
11. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular; TC dengan langkah identik ditulis sebagai perulangan atas tabel Prerequisites (8b butir 7).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 5 (Ketik Search Name baris itu, tekan Enter); langkah 7 (Klik `(←)` pada kotak Search); langkah 9 (Ketik Search Name baris itu, tekan Enter); langkah 11 (Klik `(←)` pada kotak Search).
- Langkah 1 sampai 7 berulang untuk tiga baris tabel pertama (ekspansi 3 x 7 = 21 langkah) dan langkah 8 sampai 11 untuk dua baris tabel fallback (ekspansi 2 x 4 = 8 langkah); `Verifikasi` tetap satu per klausa (S-01). Total ekspansi 29 langkah.
- Temuan untuk QA:
  - TC-FA-GRP-327 dan TC-FA-GRP-328 tidak menyebut kandidat Code yang sudah dipakai; hasil acak tidak punya nilai pasti sehingga diasersi lewat format 4 karakter huruf besar atau angka.
  - Name Code auto-generate harus literal karena token Name menentukan Code; suffix per run mengubah hasil. Butuh butir Lampiran A modul Groups (S-12).

