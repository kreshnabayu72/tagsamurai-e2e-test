---
id: TC-FA-FAAM-E2E-089-defense-in-depth-edit-request-langsung-plan-dan-excess
title: "Defense-in-Depth Edit: Request Langsung Opsi TAG Terkunci dan Asset Name Excess"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-207
  - TC-FA-FAAM-236
coverage:
  web: automated
---

# Defense-in-Depth Edit: Request Langsung Opsi TAG Terkunci dan Asset Name Excess

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control pada Client Starter pasca-downgrade (Pre-setup #16c), awal spec ini. Email dan password akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Langkah ganti akun ke Total Control pada client downgrade (Pre-setup #20) ditulis eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP sesi API aktor (token tidak dihitung sebagai sesi web) untuk request Edit langsung ke server; asersinya hanya respons server dan state data pada List (bagian 8b butir 1).
- Data Pre-setup #16c: `Grandfather Item` (TAG Type `RFID` hasil grandfathering, Total Asset 0) pada Client Starter pasca-downgrade, dirujuk lewat fixture baru `Fixture.faAssetName.grandfatherItem`. Data Pre-setup #20: client downgrade efektif (cap 3) dengan Asset Name `Excess Alpha`, `Excess Beta`, `Excess Delta`, dan `Excess Gamma` (terbaru, excess). Request Edit ditolak sehingga tidak ada perubahan data (S-06).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-207: Request Edit langsung dengan opsi TAG Type terkunci baru ditolak dan chip hasil grandfathering bertahan

1. Ketik Search `Grandfather Item`, tekan Enter
2. Catat ikon kolom TAG Type baris `Grandfather Item` (`RFID`)
3. Kirim request Edit langsung menambah TAG Type `GPS` pada `Grandfather Item` di Client Starter
4. Verifikasi server menolak dengan `409 PLAN_LIMIT_EXCEEDED` dengan `reason: "feature_locked"`
5. Muat ulang List dan Ketik Search `Grandfather Item`, tekan Enter
6. Verifikasi kolom TAG Type baris `Grandfather Item` tetap menampilkan `RFID` tanpa `GPS`

### TC-FA-FAAM-236: Edit langsung pada Asset Name excess ditolak tanpa mutasi

7. Ganti akun: login sebagai Total Control pada client downgrade (Pre-setup #20), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
8. Ketik Search `Excess Gamma`, tekan Enter
9. Catat nilai kolom baris `Excess Gamma`
10. Kirim request Edit langsung untuk `Excess Gamma`
11. Verifikasi server menolak request
12. Muat ulang List dan Ketik Search `Excess Gamma`, tekan Enter
13. Verifikasi nilai kolom baris `Excess Gamma` tidak berubah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC-FA-FAAM-207 dan 236 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec (BE mencatatnya di tingkat endpoint).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 8 untuk menemukan baris target (R-16) dan muat ulang List pada langkah 5 dan 12; ganti akun ke client downgrade pada langkah 7 (Step eksplisit, S-07).
- Request langsung ke server hanya mengasersi respons server dan state data pada List (bagian 8b butir 1). Spec ini memuat dua TC dengan akun berbeda yang berurutan karena ada Step ganti akun eksplisit dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal.
- Temuan untuk QA:
  - TC-FA-FAAM-207 dan 236 mengharapkan "Changelog tidak memuat entri baru" atas request langsung yang ditolak. Asersi ketiadaan log atas penolakan request langsung dikelola spec absence (kelas g, S-05, keputusan 2026-10-30); karena TC ini tidak ada di spec absence mana pun, klausa itu belum teruji. Pemilik suite perlu menempatkannya di spec absence.
  - TC-FA-FAAM-207 dan 236 memakai client Pre-setup #16c dan #20, tetapi tabel Pre-setup tidak memuat email akun Total Control kedua client itu; TC-FA-FAAM-236 tidak menyebut payload request Edit, sehingga spec tidak menyebut perubahan yang dikirim.
  - TC-FA-FAAM-236 Expected a "Server menolak" tidak menyebut kode status; spec mengasersi penolakan tanpa kode.
