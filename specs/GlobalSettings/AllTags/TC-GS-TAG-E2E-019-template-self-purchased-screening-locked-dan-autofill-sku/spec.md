---
id: TC-GS-TAG-E2E-019-template-self-purchased-screening-locked-dan-autofill-sku
title: "Template Self-Purchased: Screening, Locked saat Opsi Mandiri Nonaktif, dan Autofill SKU"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-49
  - TC-GS-TAG-50
  - TC-GS-TAG-51
  - TC-GS-TAG-52
coverage:
  web: automated
---

# Template Self-Purchased: Screening, Locked saat Opsi Mandiri Nonaktif, dan Autofill SKU

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun (dua client; akun pertama di hook `before`, ganti akun eksplisit di langkah 24):
  - Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`; opsi mandiri (BYO) aktif.
  - Total Control Client NoByo `totalControl_automated_qaNoByo@qwertysystem.net` (Eka Pratama), `Spectra.env.GS_TC_NOBYO_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`, lihat `suite.md` bagian Kredensial); plan Growth, opsi mandiri nonaktif.
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Data: katalog Admin Console Client A memuat SKU `SKU-GPS-01` dengan Device Name `Teltonika FMB920`, Brand `Teltonika`, Model/Type `FMB920` (dibaca saja; disediakan tim FE).
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### TC-GS-TAG-49: Screening section Self-Purchased Template

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Verifikasi section `Self-Purchased Template` collapsed pada kondisi awal
3. Klik header section `Self-Purchased Template`
4. Verifikasi section terbuka
5. Verifikasi urutan field: `Device Name *`, `SKU`, `Brand *`, `Model/Type`
6. Verifikasi field `Device Name *` dengan placeholder `Search and select device name...`
7. Verifikasi field `SKU` dengan placeholder `Search and select SKU (optional)...`
8. Verifikasi field `Brand *` dengan placeholder `Search or add a brand...`
9. Verifikasi field `Model/Type` dengan placeholder `Search or add a model/type...`
10. Verifikasi tanda `*` pada Brand tampil selama SKU kosong

### TC-GS-TAG-51: Memilih SKU mengisi Brand dan Model/Type

11. Pilih SKU `SKU-GPS-01`
12. Verifikasi field Device Name terisi `Teltonika FMB920` sesuai katalog
13. Verifikasi field Brand terisi `Teltonika` sesuai katalog
14. Verifikasi field Model/Type terisi `FMB920` sesuai katalog
15. Verifikasi field Device Name, Brand, dan Model/Type terkunci (tidak dapat diedit) selama SKU terisi
16. Verifikasi tanda `*` pada Brand hilang

### TC-GS-TAG-52: Mengosongkan SKU membuat Brand wajib kembali

17. Kosongkan SKU
18. Verifikasi nilai Device Name hasil autofill dikosongkan
19. Verifikasi nilai Brand hasil autofill dikosongkan
20. Verifikasi nilai Model/Type hasil autofill dikosongkan
21. Verifikasi field Device Name, Brand, dan Model/Type dapat diedit kembali
22. Verifikasi tanda `*` pada Brand tampil kembali
23. Kembali ke List: klik item sidebar `TAG` (staging kosong)

### TC-GS-TAG-50: Template Locked saat opsi mandiri nonaktif

24. Ganti akun: logout, login sebagai Total Control Client NoByo (`Spectra.env.GS_TC_NOBYO_PASSWORD`)
25. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
26. Buka section `Self-Purchased Template`
27. Hover section `Self-Purchased Template`
28. Verifikasi tooltip `Self-purchased activation is not enabled for your account. Contact your administrator.`
29. Verifikasi seluruh field Template disabled
30. Verifikasi field Template tetap tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (screening Template).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: TC-49, TC-51, TC-52 pada satu sesi GPS Client A (section Template tetap terbuka dari TC-49 sehingga TC-51 dan TC-52 tidak membuka ulang sesi); TC-50 paling akhir karena butuh ganti akun ke Client NoByo (langkah 24). Tooltip TC-50 diasersi sebelum langkah yang mengubah state (butir 5 bagian 8b).
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Kembali ke List` (staging kosong, tanpa dialog); langkah `Buka section` pada TC-50 mengikuti TC langkah 4.
- Temuan untuk QA:
  - TC-51 Expected b menyebut ketiga field "terkunci", TC-50 Expected a menyebut "disabled"; TC tidak menyatakan apakah keduanya tampilan yang sama. Spec menulis kata kerja sesuai TC masing-masing.
  - TC-52 tidak memiliki precondition katalog; SKU `SKU-GPS-01` dipakai dari TC-51.
