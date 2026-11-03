---
id: TC-FA-FAAM-E2E-105-popup-detail-progres-kepatuhan-tag-type-format-dan-bentuk-tunggal
title: "Popup Detail: Progres Kepatuhan TAG Type, Format Baris, Read-Only, Modal Edit Tanpa Progres, dan Bentuk Tunggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-830
  - TC-FA-FAAM-832
coverage:
  web: automated
---

# Popup Detail: Progres Kepatuhan TAG Type, Format Baris, Read-Only, Modal Edit Tanpa Progres, dan Bentuk Tunggal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup yang hanya dibaca (modal Edit hanya dibuka lalu ditutup tanpa perubahan sehingga Last Updated tidak berubah; S-06):
  - Pre-setup #38: `Excavator 20 Ton` (TAG Type `RFID`), 40 aset `Active` dalam scope client: Group `Plant A` 20 aset (18 ber-Tag `Paired` RFID, 2 `Not Paired Yet`) dan Group `Plant B` 20 aset (15 ber-Tag `Paired` RFID, 5 ber-Tag `Paired` QR yang Non-standard). `[Compliant]` 33, `[N]` 40. Fixture `Fixture.faAssetName.excavator`.
  - Pre-setup #38b: `Drill Press` (TAG Type `QR`, 1 aset `Active` ber-Tag `Paired` QR; `[Compliant]` 1, `[N]` 1) dan `Drill Press Unpaired` (TAG Type `QR`, 1 aset `Active` `Not Paired Yet`; `[Compliant]` 0, `[N]` 1).
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-830: Popup Detail menampilkan progres kepatuhan TAG Type dan Modal Edit tidak memuatnya

1. Ketik Search `Excavator 20 Ton`, tekan Enter
2. Klik nama `Excavator 20 Ton`
3. Verifikasi tepat di bawah nilai TAG Type (icon `RFID`) tampil satu baris teks `33 / 40 assets match the TAG type`
4. Verifikasi urutan grid Identitas Utama tetap Asset Name, Code, Category, TAG Type, UoM, Default Addon, Default Label
5. Verifikasi baris progres bukan field grid tersendiri
6. Verifikasi baris progres read-only tanpa ikon, tautan, atau aksi
7. Arahkan pointer ke baris progres
8. Verifikasi tidak ada tooltip yang tampil
9. Klik baris progres
10. Verifikasi klik tidak membuka apa pun (Popup Detail tetap sama)
11. Verifikasi penyebut baris progres adalah 40, menghitung seluruh aset `Active` Asset Name itu (Plant A 20 dan Plant B 20), bukan 20 per group
12. Klik icon `[✕]` untuk menutup popup
13. Klik `⋯` baris `Excavator 20 Ton` lalu `Edit`
14. Verifikasi Modal Edit memuat field TAG Type
15. Verifikasi Modal Edit tidak memuat baris progres kepatuhan, termasuk area di bawah field TAG Type
16. Klik `[✕]` pada Modal Edit tanpa mengubah apa pun
17. Verifikasi sel TAG Type baris `Excavator 20 Ton` di Asset Name List hanya memuat icon `RFID` tanpa teks progres

### TC-FA-FAAM-832: Progres kepatuhan memakai bentuk tunggal bila [N] = 1

18. Ganti isi kotak search dengan `Drill Press`, tekan Enter
19. Klik nama `Drill Press`
20. Verifikasi baris progres `1 / 1 asset matches the TAG type`
21. Klik icon `[✕]` untuk menutup popup
22. Klik nama `Drill Press Unpaired`
23. Verifikasi baris progres `0 / 1 asset matches the TAG type`
24. Verifikasi kedua anggota memakai bentuk tunggal `asset matches`, bukan `assets match`
25. Klik icon `[✕]` untuk menutup popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 18), `[✕]` menutup popup (langkah 12, 21, 25), dan `[✕]` menutup Modal Edit yang tidak dirty sehingga dialog Unsaved Changes tidak muncul (langkah 16).
- Asersi tooltip pada langkah 8 ditulis tepat sesudah pemicu hover pada langkah 7 (bagian 8b butir 5 dan 11); asersi absence pada langkah 15 memakai field TAG Type pada langkah 14 sebagai anchor, dan pada langkah 17 memakai icon `RFID` pada sel yang sama sebagai anchor.
- Temuan untuk QA:
  - TC-FA-FAAM-830 Expected d menyebut `[N]` 40 bukan 20 per group; spec mengamati penyebut baris progres (langkah 11) karena TC tidak memberi cara lain menghitung aset `Active` dari UI.
  - TC-FA-FAAM-830 langkah 4 menutup Modal Edit "tanpa mengubah apa pun"; spec mengandaikan form tidak dirty sehingga tidak ada dialog Unsaved Changes.
  - TC-FA-FAAM-832 Expected c ("bukan `assets match`") sudah tercakup oleh teks persis pada Expected a dan b; spec tetap menuliskannya sebagai langkah terpisah (S-01).
