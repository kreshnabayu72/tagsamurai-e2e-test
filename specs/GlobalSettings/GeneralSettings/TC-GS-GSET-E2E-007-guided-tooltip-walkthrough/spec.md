---
id: TC-GS-GSET-E2E-007-guided-tooltip-walkthrough
title: "Guided Tooltip 2 langkah: konten verbatim dan siklus penuh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-16
  - TC-GS-GSET-17
coverage:
  web: automated
mock: true
---

# Guided Tooltip: konten 2 langkah dan siklus penuh (trigger, navigasi, exit, a11y)

## Prerequisites

- Spec ini dijalankan dengan `Mode: mock`. Alur Guided Tooltip adalah tampilan murni; tidak perlu
  interaksi backend untuk menggerakkan percakapan tooltip.
- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- React state "first-run" disimulasikan: untuk skenario first-visit, flag penutupan tooltip tidak
  ter-set; untuk skip-selesai, flag ter-set.
- Isi Title/Description langkah diambil dari fixture `Fixture.globalSettingsGeneralSettings.guidedTooltip`,
  tidak ditulis verbatim di spec (PRD §4.7 menuliskannya, dikunci aturan Guided Tooltip BahasaInggris).

## Test Steps

### Trigger otomatis first-visit

1. Buka `Global Settings > General Settings` setelah memastikan belum ada flag "tooltip pernah
   ditutup"
2. Verifikasi Guided Tooltip muncul otomatis (auto first-visit)
3. Verifikasi Step 1 menargetkan field `Currency Code` dengan title `Set Your Regional Format`
4. Verifikasi Step 2 (setelah maju) menargetkan field `Session Idle Timeout` dengan title
   `Control Session Timeout`
5. Verifikasi description tiap langkah ditampilkan verbatim sesuai fixture

### Navigasi maju/mundur, skip, done

6. Verifikasi kontrol navigasi tampil (Next/Back/Skip/Done sesuai state)
7. Klik Back saat di step 2: verifikasi kembali ke step 1 (target Currency Code)
8. Klik maju sampai step terakhir lalu klik `[Done]`
9. Verifikasi tooltip hilang dan flag "pernah ditutup" ter-set
10. Muat ulang halaman: verifikasi tooltip TIDAK muncul lagi (flag)

### Trigger manual via `[?]` dan exit tanpa selesai (resize)

11. Klik ikon `[?]` di field terkait
12. Verifikasi tooltip muncul kembali (trigger manual)
13. Simulasikan resize/exit tanpa menyelesaikan: ubah ukuran viewport (resize)
14. Verifikasi tooltip tertutup namun flag "pernah ditutup" TIDAK ter-set
15. Muat ulang halaman dan buka lagi: verifikasi tooltip muncul kembali (karena tidak selesai)

### Keyboard dan aksesibilitas

16. Buka tooltip lagi; verifikasi navigasi keyboard berfungsi: `Esc` menutup, `Enter`/panah
    memajukan/memilih, sesuai pola
17. Verifikasi atribut peran/title pada elemen sasaran terbaca oleh assistive tech (target fokus
    berada pada elemen yang benar)

## Notes

- Spec ini mencakup TC-GS-GSET-16 (konten 2 step verbatim) dan TC-GS-GSET-17 (siklus lengkap). Detail
  siklus mengikuti PRD §4.7 dan `prd-conventions.md` §16. Title diekspektasi dari fixture; linter
  spec mengharuskan deskripsi dijalankan verbatim oleh script, bukan ditulis ulang di spec.