---
id: TC-GS-TAG-E2E-048-selection-limit-checkbox-diblokir-dan-select-all-di-cap
title: "Selection Limit: Checkbox ke-(L+1) Diblokir dan Select All Lintas Halaman di-Cap"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-157
  - TC-GS-TAG-158
coverage:
  web: automated
---

# Selection Limit: Checkbox ke-(L+1) Diblokir dan Select All Lintas Halaman di-Cap

## Prerequisites

- Mode: FE+BE (backend nyata; kelas e, volume data khusus). Spec ini tidak menghapus data.
- Akun aktor: Total Control Client Limit (Irfan Maulana) `totalControl_automated_qaLimit@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup: Client Limit dengan Selection Limit L disetel ke nilai minimum System Limits dan N tag Not Paired eligible dengan N > L (kelas e: nilai minimum System Limits disediakan tim FE/BE sehingga dibutuhkan lebih dari L baris Not Paired; Q-7). Nilai L dan N diturunkan dari seeding dan pengaturan limit, tidak dibaca dari satu halaman tabel (S-11 butir N total). Tag memakai identifier tetap Client Limit (S-12, Q-4).
- Kemampuan teknis (disediakan tim FE/BE): penyetelan Selection Limit Client Limit ke nilai minimum System Limits dan pembacaan nilai L; seed lebih dari L baris tag Available di Tab Not Paired; reset idempotent seed tersebut; pembacaan nilai N.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan Selection Limit Client Limit ke nilai awal dan kembalikan seed tag Client Limit.
- Suite serial (`parallel: false`). State global yang diubah: Selection Limit Client Limit (Admin Console); dipulihkan hook `after`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-157: Checkbox ke-(L+1) disabled saat dicentang manual

1. Centang baris Not Paired satu per satu dari baris pertama sampai baris ke-L, berpindah ke halaman tabel berikutnya sesuai urutan baris
2. Coba centang baris ke-(L+1)
3. Verifikasi checkbox baris ke-(L+1) disabled
4. Hover checkbox baris ke-(L+1)
5. Verifikasi tooltip `You've reached the maximum selection of L rows.` dengan L berisi nilai Selection Limit berlaku
6. Verifikasi L baris pertama tetap tercentang
7. Verifikasi Bulk Action Bar tetap aktif
8. Klik `(✕)` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-TAG-158: Select All lintas halaman di-cap otomatis

9. Centang baris Not Paired pertama
10. Klik `Select All (N records)`
11. Verifikasi seleksi di-cap ke L baris pertama
12. Verifikasi toast error persisten `Error, only the first L of N rows were selected. Narrow your filter to include the rest.` dengan L dan N berisi nilai berlaku
13. Verifikasi Bulk Action Bar tetap muncul
14. Buka dropdown `Bulk Action`
15. Verifikasi dropdown dapat dipakai (entri `Delete` tampil)
16. Tutup dropdown
17. Klik `Unselect All`

## Notes

- Mode: FE+BE. Kelas e (Selection Limit, lebih dari L baris). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1 mengulang pencentangan satu per satu sampai baris ke-L (L dari seeding; Prerequisites); diulang sebanyak L kali, berpindah halaman mengikuti urutan baris.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 8 dan 17 (membersihkan seleksi), 9 (mencentang baris pertama supaya Bulk Action Bar dan `Select All (N records)` tampil; bar hilang bila seleksi kosong), 16 (menutup dropdown). Langkah 14 dan 15 menerjemahkan Expected "bar tetap muncul dan dapat dipakai" (TC-GS-TAG-158 butir b): bukti "dapat dipakai" memakai dropdown `Bulk Action`.
- Asersi tambahan di luar Expected TC (S-03): langkah 15 (isi dropdown) sebagai bukti "dapat dipakai", dicatat di sini.
- Temuan untuk QA:
  - Q-7: TC tidak memberi angka L ("nilai berlaku", "disetel ke minimum"); L dan seed lebih dari L disediakan tim FE/BE.
  - TC-GS-TAG-158 Expected a menyebut toast error "persisten" tanpa durasi atau cara membuktikan persistensi; spec hanya mengasersi toast tampil dengan teks yang ditetapkan.
  - TC-GS-TAG-157 Expected a mengatakan L adalah "nilai berlaku" sedangkan Data Uji menulis "L = Selection Limit Client Limit"; sama maknanya, dicatat sebagai informasi.
  - TC-GS-TAG-158 tidak menyebut seleksi awal sebelum klik `Select All ([N] records)`, padahal Bulk Action Bar hilang bila seleksi kosong; spec mencentang baris pertama lebih dulu (langkah 9).
  - Post Condition semua TC bernilai `-`.
